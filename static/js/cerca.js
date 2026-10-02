/* Ricerca interna di raziel.news — un file per tutte le lingue.
   Legge l'indice JSON della lingua della pagina (attributo data-indice del
   modulo) e filtra e ordina lato client. Nessuna libreria, nessun servizio
   esterno, nessuna richiesta a terzi: il lettore scarica un file dal sito.

   Come cerca: tutte le parole digitate devono comparire (AND). Il peso
   distingue dove compaiono — titolo 8 (12 se il titolo inizia con la parola),
   tag e temi 6, sommario 3, corpo 1 — e i risultati sono ordinati per punteggio
   e, a parità, dal più recente.

   Le frasi dell'interfaccia e il percorso dell'indice arrivano da attributi
   data-* sul modulo (i18n e relLangURL nel template): qui non c'è testo fisso
   e non c'è percorso fisso, così la stessa ricerca serve italiano e inglese. */

(function () {
  'use strict';

  var modulo = document.getElementById('cerca-form');
  if (!modulo) { return; }

  var input = document.getElementById('cerca-input');
  var stato = document.getElementById('cerca-stato');
  var elenco = document.getElementById('cerca-risultati');
  var LIMITE = 30;

  var indice = null;

  function frase(nome) { return modulo.getAttribute('data-' + nome) || ''; }

  function normalizza(testo) {
    return (testo || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
  }

  function terminiDa(interrogazione) {
    return normalizza(interrogazione)
      .split(/[^a-z0-9]+/)
      .filter(function (t) { return t.length > 1; });
  }

  /* La data si scrive nella lingua della pagina, non in formato tecnico:
     "2 ottobre 2026" in italiano, "October 2, 2026" in inglese. */
  function dataInChiaro(iso) {
    if (!iso) { return ''; }
    try {
      var d = new Date(iso + 'T12:00:00');
      if (isNaN(d.getTime())) { return iso; }
      return d.toLocaleDateString(frase('lingua') || undefined,
        { day: 'numeric', month: 'long', year: 'numeric' });
    } catch (e) { return iso; }
  }

  function punteggio(voce, termini) {
    var titolo = normalizza(voce.titolo);
    var sommario = normalizza(voce.sommario);
    var etichette = normalizza((voce.tag || []).concat(voce.temi || []).join(' '));
    var corpo = normalizza(voce.testo);
    var totale = 0;
    for (var i = 0; i < termini.length; i++) {
      var t = termini[i];
      var p = 0;
      if (titolo.indexOf(t) !== -1) { p = titolo.indexOf(t) === 0 ? 12 : 8; }
      else if (etichette.indexOf(t) !== -1) { p = 6; }
      else if (sommario.indexOf(t) !== -1) { p = 3; }
      else if (corpo.indexOf(t) !== -1) { p = 1; }
      if (p === 0) { return 0; }
      totale += p;
    }
    return totale;
  }

  /* Evidenzia le parole trovate costruendo nodi, senza innerHTML:
     il testo dell'articolo non viene mai interpretato come HTML. */
  function evidenzia(testo, termini) {
    var frammento = document.createDocumentFragment();
    var semplice = normalizza(testo);
    var punti = [];
    termini.forEach(function (t) {
      var da = 0, pos;
      while ((pos = semplice.indexOf(t, da)) !== -1) {
        punti.push([pos, pos + t.length]);
        da = pos + t.length;
      }
    });
    if (!punti.length) { frammento.appendChild(document.createTextNode(testo)); return frammento; }
    punti.sort(function (a, b) { return a[0] - b[0]; });
    var fusi = [], corrente = punti[0];
    for (var i = 1; i < punti.length; i++) {
      if (punti[i][0] <= corrente[1]) { corrente[1] = Math.max(corrente[1], punti[i][1]); }
      else { fusi.push(corrente); corrente = punti[i]; }
    }
    fusi.push(corrente);
    var cursore = 0;
    fusi.forEach(function (p) {
      if (p[0] > cursore) { frammento.appendChild(document.createTextNode(testo.slice(cursore, p[0]))); }
      var mark = document.createElement('mark');
      mark.textContent = testo.slice(p[0], p[1]);
      frammento.appendChild(mark);
      cursore = p[1];
    });
    if (cursore < testo.length) { frammento.appendChild(document.createTextNode(testo.slice(cursore))); }
    return frammento;
  }

  function mostraRisultati(interrogazione) {
    var termini = terminiDa(interrogazione);
    elenco.textContent = '';

    if (!termini.length) {
      stato.textContent = (interrogazione.trim() ? frase('almeno-due') + ' ' : '') + frase('aiuto');
      return;
    }
    if (!indice) { stato.textContent = frase('attesa'); return; }

    var trovate = [];
    indice.forEach(function (voce) {
      var p = punteggio(voce, termini);
      if (p > 0) { trovate.push({ voce: voce, p: p }); }
    });
    trovate.sort(function (a, b) {
      return b.p - a.p || (a.voce.data < b.voce.data ? 1 : -1);
    });

    if (!trovate.length) {
      stato.textContent = frase('vuoto');
      return;
    }

    stato.textContent = trovate.length + ' ' +
      (trovate.length === 1 ? frase('risultato') : frase('risultati')) +
      (trovate.length > LIMITE ? ' (' + frase('primi') + ' ' + LIMITE + ')' : '');

    trovate.slice(0, LIMITE).forEach(function (r) {
      var voce = r.voce;
      var li = document.createElement('li');
      li.className = 'cerca-voce';

      var titolo = document.createElement('a');
      titolo.className = 'cerca-titolo';
      titolo.href = voce.url;
      titolo.appendChild(evidenzia(voce.titolo, termini));

      var meta = document.createElement('span');
      meta.className = 'cerca-meta';
      meta.textContent = dataInChiaro(voce.data) +
        (voce.temi && voce.temi.length ? ' · ' + voce.temi.join(', ') : '');

      var sommario = document.createElement('span');
      sommario.className = 'cerca-sommario';
      sommario.appendChild(evidenzia(voce.sommario || '', termini));

      li.appendChild(titolo);
      li.appendChild(meta);
      li.appendChild(sommario);
      elenco.appendChild(li);
    });
  }

  function aggiornaIndirizzo(interrogazione) {
    if (!window.history || !window.history.replaceState) { return; }
    var url = interrogazione.trim()
      ? window.location.pathname + '?q=' + encodeURIComponent(interrogazione.trim())
      : window.location.pathname;
    window.history.replaceState({}, '', url);
  }

  var attesa = null;
  input.addEventListener('input', function () {
    window.clearTimeout(attesa);
    attesa = window.setTimeout(function () {
      mostraRisultati(input.value);
      aggiornaIndirizzo(input.value);
    }, 150);
  });
  modulo.addEventListener('submit', function (evento) {
    evento.preventDefault();
    window.clearTimeout(attesa);
    mostraRisultati(input.value);
    aggiornaIndirizzo(input.value);
  });

  fetch(frase('indice') || '/index.json')
    .then(function (r) {
      if (!r.ok) { throw new Error('HTTP ' + r.status); }
      return r.json();
    })
    .then(function (dati) {
      indice = (dati && dati.voci) || [];
      var iniziale = new URLSearchParams(window.location.search).get('q');
      if (iniziale) {
        input.value = iniziale;
        mostraRisultati(iniziale);
      } else {
        stato.textContent = indice.length + ' ' + frase('voci') + ' ' + frase('aiuto');
      }
    })
    .catch(function (errore) {
      stato.textContent = frase('errore') + ' (' + errore.message + '). ' + frase('ripiego');
    });
})();
