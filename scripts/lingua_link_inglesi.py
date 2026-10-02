#!/usr/bin/env python3
"""Riscrive i link interni delle versioni inglesi: da pagina italiana a pagina inglese.

Perche' serve: uno stadio `pipeline-traduzione` scrive la versione inglese di un articolo
collegato a un altro articolo che, in quel momento, non ha ancora la sua traduzione. In quel
caso il link resta all'italiano (corretto: la pagina inglese non esiste ancora). Quando la
traduzione arriva, il link va spostato sulla versione inglese, altrimenti il lettore inglese
esce dalla lingua del sito cliccando un rimando interno.

Regola di sicurezza: si riscrive **solo** se il bersaglio inglese e' dichiarato nel frontmatter
della versione inglese (`url: "/en/..."`) e solo per link presenti nel corpo. Nessuna
invenzione: se la coppia non si trova, il link resta com'era.

Uso:
    python3 scripts/lingua_link_inglesi.py            # mostra cosa cambierebbe, non scrive
    python3 scripts/lingua_link_inglesi.py --scrivi   # applica
"""
import pathlib
import re
import sys
import unicodedata

POSTS = pathlib.Path(__file__).resolve().parent.parent / "content" / "posts"
SCRIVI = "--scrivi" in sys.argv
SITO = "https://raziel.news"


def slugify(testo):
    """Stessa resa di Hugo per il permalink :title (minuscole, accenti tolti, trattini)."""
    testo = unicodedata.normalize("NFKD", testo)
    testo = "".join(c for c in testo if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", testo.lower()).strip("-")


def frontmatter(percorso):
    """(dict grezzo, corpo) del frontmatter YAML, senza dipendenze esterne."""
    testo = percorso.read_text(encoding="utf-8")
    if not testo.startswith("---"):
        return {}, testo
    parti = testo.split("---", 2)
    if len(parti) < 3:
        return {}, testo
    fm = {}
    for riga in parti[1].splitlines():
        if ":" not in riga:
            continue
        chiave, valore = riga.split(":", 1)
        fm[chiave.strip()] = valore.strip().strip('"').strip("'")
    return fm, parti[2]


def percorso_italiano(fm):
    """Percorso pubblico della pagina italiana: `url:` se c'e', altrimenti dal titolo."""
    if fm.get("url"):
        return fm["url"].rstrip("/") + "/"
    data, titolo = fm.get("date", ""), fm.get("title", "")
    if len(data) < 7 or not titolo:
        return None
    return f"/{data[:4]}/{data[5:7]}/{slugify(titolo)}/"


def costruisci_mappa():
    """{percorso italiano: percorso inglese} per ogni articolo che ha la traduzione."""
    mappa, senza_url = {}, []
    for en in sorted(POSTS.glob("*.en.md")):
        it = POSTS / (en.name[: -len(".en.md")] + ".md")
        if not it.exists():
            continue
        fm_en, _ = frontmatter(en)
        destinazione = (fm_en.get("url") or "").rstrip("/")
        if not destinazione:
            senza_url.append(en.name)
            continue
        fm_it, _ = frontmatter(it)
        origine = percorso_italiano(fm_it)
        if origine:
            mappa[origine] = destinazione + "/"
    return mappa, senza_url


def riscrivi(testo, mappa):
    """Applica le sostituzioni e ritorna (testo nuovo, elenco sostituzioni)."""
    sostituzioni = []
    for origine, destinazione in mappa.items():
        for forma in (f"]({origine})", f"]({SITO}{origine})"):
            quante = testo.count(forma)
            if quante:
                testo = testo.replace(forma, forma.replace(origine, destinazione))
                sostituzioni.append((origine, destinazione, quante))
    return testo, sostituzioni


def main():
    if not POSTS.is_dir():
        print(f"cartella non trovata: {POSTS}")
        return 1
    mappa, senza_url = costruisci_mappa()
    print(f"coppie italiano → inglese con percorso dichiarato: {len(mappa)}")
    if senza_url:
        print(f"versioni inglesi senza `url:` (saltate): {', '.join(senza_url)}")

    totale_link, file_toccati = 0, 0
    for en in sorted(POSTS.glob("*.en.md")):
        testo = en.read_text(encoding="utf-8")
        nuovo, sostituzioni = riscrivi(testo, mappa)
        if not sostituzioni:
            continue
        file_toccati += 1
        for origine, destinazione, quante in sostituzioni:
            totale_link += quante
            print(f"  {en.name}: {origine} → {destinazione} ({quante})")
        if SCRIVI:
            en.write_text(nuovo, encoding="utf-8")

    azione = "riscritti" if SCRIVI else "da riscrivere (nessuna modifica scritta)"
    print(f"\nlink interni {azione}: {totale_link} in {file_toccati} articoli inglesi")
    if not SCRIVI and totale_link:
        print("rilancia con --scrivi per applicare")
    return 0


if __name__ == "__main__":
    sys.exit(main())
