// Card di condivisione = la scheda dell'articolo del sito, fotografata.
//
// Legge il foglio /og-schede/ (e /en/og-schede/) di un build temporaneo fatto
// con scripts/og-schede/config.yaml: ogni articolo è disegnato dal partial
// post-card.html con i CSS veri del sito, in una cornice da 1200x630.
// Qui si fotografa ogni cornice in static/images/og/v4/<nome>.png (italiano)
// e static/images/og/v4/en/<nome>.png (inglese). extra-head.html dà a v4 la
// priorità più alta, quindi og:image e twitter:image puntano a queste.
//
// Uso:
//   hugo --minify --config hugo.yaml,scripts/og-schede/config.yaml -d /tmp/og
//   node scripts/og_schede.mjs /tmp/og [nome-articolo]
//
// Chrome: variabile CHROME, altrimenti i percorsi noti (CI: google-chrome).
// Nessun pacchetto npm: CDP via WebSocket nativo di Node >= 22 e un server
// HTTP minimo (i CSS del sito usano percorsi assoluti /css/..., /fonts/...,
// quindi file:// non basterebbe).
import { spawn, execFileSync } from 'node:child_process';
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';

const [PUB, SOLO = ''] = process.argv.slice(2);
if (!PUB || !fs.existsSync(path.join(PUB, 'og-schede', 'index.html'))) {
  console.error('uso: node scripts/og_schede.mjs <cartella del build con og-schede> [nome]');
  process.exit(2);
}
const RADICE = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const USCITA = path.join(RADICE, 'static', 'images', 'og', 'v4');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function trovaChrome() {
  if (process.env.CHROME) return process.env.CHROME;
  const candidati = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser',
    '/root/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome'];
  for (const c of candidati) {
    if (c.startsWith('/') && fs.existsSync(c)) return c;
    try { return execFileSync('which', [c]).toString().trim(); } catch {}
  }
  return null;
}

const TIPI = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(PUB, p);
  if (!f.startsWith(path.resolve(PUB)) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': TIPI[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const BASE = `http://127.0.0.1:${server.address().port}`;

const CHROME = trovaChrome();
if (!CHROME) { console.error('ATTENZIONE: nessun Chrome trovato'); process.exit(1); }
const PORTA = 9300 + Math.floor(Math.random() * 500);
const profilo = fs.mkdtempSync(path.join(process.env.TMPDIR || '/tmp', 'og-schede-'));
const chrome = spawn(CHROME, ['--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
  `--remote-debugging-port=${PORTA}`, `--user-data-dir=${profilo}`, 'about:blank'], { stdio: 'ignore' });

let wsUrl;
for (let i = 0; i < 120 && !wsUrl; i++) {
  try {
    const lista = await (await fetch(`http://127.0.0.1:${PORTA}/json/list`)).json();
    wsUrl = lista.find((x) => x.type === 'page')?.webSocketDebuggerUrl;
  } catch {}
  if (!wsUrl) await sleep(250);
}
if (!wsUrl) { console.error('chrome non risponde'); process.exit(1); }
const ws = new WebSocket(wsUrl);
await new Promise((r, e) => { ws.onopen = r; ws.onerror = e; });
let ultimo = 0; const attese = new Map();
ws.onmessage = (ev) => { const m = JSON.parse(ev.data); if (attese.has(m.id)) { attese.get(m.id)(m); attese.delete(m.id); } };
const cdp = (method, params = {}) => new Promise((r) => { const id = ++ultimo; attese.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
const valuta = async (expr) => (await cdp('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;

await cdp('Page.enable'); await cdp('Runtime.enable');
await cdp('Emulation.setDeviceMetricsOverride', { width: 1200, height: 630, deviceScaleFactor: 1, mobile: false });

let fatte = 0, ridotte = 0; const errori = [];
for (const [lingua, percorso] of [['it', '/og-schede/'], ['en', '/en/og-schede/']]) {
  await cdp('Page.navigate', { url: BASE + percorso });
  for (let i = 0; i < 120; i++) { if (await valuta(`document.body && document.body.dataset.pronto`) === '1') break; await sleep(250); }
  const nomi = await valuta(`[...document.querySelectorAll('.og-cornice')].map(c => c.dataset.nome)`) || [];
  const cartella = lingua === 'it' ? USCITA : path.join(USCITA, lingua);
  fs.mkdirSync(cartella, { recursive: true });
  for (let i = 0; i < nomi.length; i++) {
    if (SOLO && nomi[i] !== SOLO) continue;
    // Una cornice alla volta in cima alla pagina, le altre nascoste: niente
    // scroll (il tema ha scroll-behavior:smooth, e una foto scattata a metà
    // scorrimento prende due schede tagliate). Poi si aspettano le immagini.
    const scala = await valuta(`(async () => {
      const tutte = document.querySelectorAll('.og-cornice');
      tutte.forEach((x, j) => { x.style.display = j === ${i} ? 'flex' : 'none'; });
      const c = tutte[${i}];
      c.querySelectorAll('img').forEach(im => { im.loading = 'eager'; });
      await Promise.all([...c.querySelectorAll('img')].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; })));
      await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
      return window.scrollY === 0 && c.getBoundingClientRect().top === 0 ? c.dataset.scala : 'fuori'; })()`);
    if (scala === 'fuori') { errori.push(`${lingua}/${nomi[i]} (cornice non in cima)`); continue; }
    const foto = await cdp('Page.captureScreenshot', { format: 'png', clip: { x: 0, y: 0, width: 1200, height: 630, scale: 1 } });
    if (!foto.result?.data) { errori.push(`${lingua}/${nomi[i]}`); continue; }
    fs.writeFileSync(path.join(cartella, `${nomi[i]}.png`), Buffer.from(foto.result.data, 'base64'));
    fatte++; if (Number(scala) < 1) ridotte++;
  }
  console.log(`${lingua}: ${nomi.length} schede nel foglio`);
}
console.log(`card scritte: ${fatte} in ${path.relative(RADICE, USCITA)} (ridotte in scala per stare in 1200x630: ${ridotte})`);
if (errori.length) console.log(`ATTENZIONE: non fotografate ${errori.length}: ${errori.join(', ')}`);
// Chrome scrive nel profilo mentre si chiude: si aspetta l'uscita, e la
// pulizia non deve mai far fallire un giro in cui le card sono già scritte.
await new Promise((r) => { chrome.once('exit', r); chrome.kill(); setTimeout(r, 3000); });
server.close();
try { fs.rmSync(profilo, { recursive: true, force: true, maxRetries: 3, retryDelay: 200 }); } catch {}
process.exit(errori.length ? 1 : 0);
