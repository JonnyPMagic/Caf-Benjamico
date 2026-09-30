"""Erzeugt aus der fertigen Website die Bausteine für Jimdo Creator (Ordner jimdo/).

Im Projektordner ausführen:
    python3 tools/build_jimdo.py

Ergebnis:
    jimdo/layout.html      -> Jimdo: Design > Layout > Eigenes Layout, Reiter HTML
    jimdo/layout.css       -> Jimdo: Design > Layout > Eigenes Layout, Reiter CSS
    jimdo/head.html        -> Jimdo: Einstellungen > Head bearbeiten (ganze Website)
    jimdo/seiten/*.html    -> je Seite in ein Element "Widget/HTML" einfügen

Bild- und Schrift-Adressen stehen in jimdo/dateien.json (nach dem Hochladen
bei Jimdo dort eintragen und das Skript erneut ausführen). Die Datei wird nur
angelegt, wenn sie fehlt, eingetragene Adressen bleiben also erhalten.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "jimdo"

# Adressen der Seiten bei Jimdo. Jimdo bildet sie aus dem Seitennamen in der
# Navigation; falls eine Seite dort anders heißt, hier anpassen.
PAGES = {
    "index.html": "/",
    "speisekarte.html": "/speisekarte/",
    "angebot.html": "/unser-angebot/",
    "trauerfeiern.html": "/trauerfeiern/",
    "feiern.html": "/private-feiern/",
    # Impressum und Datenschutz sind bei Jimdo feste Systemseiten.
    "impressum.html": "/about/",
    "datenschutz.html": "/j/privacy",
}

ASSETS = [
    "assets/fonts/bricolage-grotesque.woff2",
    "assets/fonts/cormorant-garamond-latin-wght-normal.woff2",
    *sorted(str(p.relative_to(ROOT)) for p in (ROOT / "assets/img").glob("*.webp")),
]

RESERVATION = "https://mylightspeed.app/reservation/7c834812-f92a-4272-9d08-bcf47c01e505/reservation"


def load_files():
    """Liest jimdo/dateien.json; legt sie beim ersten Lauf mit leeren Einträgen an."""
    OUT.mkdir(exist_ok=True)
    path = OUT / "dateien.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    data.setdefault("_basis", "")
    for a in ASSETS:
        data.setdefault(a, "")
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return data


FILES = {}
MISSING = set()


def asset_url(path):
    if FILES.get(path):
        return FILES[path]
    if FILES.get("_basis"):
        return FILES["_basis"].rstrip("/") + "/" + path
    MISSING.add(path)
    return path


def rewrite(html):
    """Bild-Adressen und interne Links auf Jimdo umstellen."""
    html = re.sub(r"assets/(?:img|fonts)/[\w.-]+", lambda m: asset_url(m.group(0)), html)

    def link(m):
        page, frag = m.group(1), m.group(2) or ""
        return f'href="{PAGES[page]}{frag}"' if page in PAGES else m.group(0)

    return re.sub(r'href="([\w-]+\.html)(#[\w-]+)?"', link, html)


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def dedent(block):
    lines = block.strip("\n").splitlines()
    indent = min(len(l) - len(l.lstrip()) for l in lines if l.strip())
    return "\n".join(l[indent:] for l in lines)


def page_snippet(name):
    """Inhalt von <main> einer Seite als Baustein für ein Widget/HTML-Element."""
    src = read(name)
    m = re.search(r'<main id="main"(?: class="([\w -]+)")?>(.*?)</main>', src, re.S)
    cls, body = m.group(1), dedent(m.group(2))
    if cls:
        body = f'<div class="{cls}">\n' + "\n".join("  " + l if l else l for l in body.splitlines()) + "\n</div>"
    # Seitenbezogene strukturierte Daten (z. B. FAQ) mitnehmen; die Café-Daten stehen in head.html.
    ld = [s for s in re.findall(r'<script type="application/ld\+json">.*?</script>', src, re.S)
          if "CafeOrCoffeeShop" not in s]
    head = (f"<!-- Cafe Benjamico – {name} für Jimdo (Widget/HTML). Erzeugt von tools/build_jimdo.py, "
            "bitte dort ändern. -->\n")
    return head + body + "\n" + "".join("\n" + s + "\n" for s in ld)


def layout():
    index = read("index.html")
    sprite = dedent(re.search(r'[ \t]*<svg width="0".*?</svg>(?=\s*<a class="skip")', index, re.S).group(0))
    grid = dedent(re.search(r'[ \t]*<div class="container footer__grid">.*?\n    </div>(?=\s*<div class="container footer__bottom">)',
                            index, re.S).group(0))
    script = read("assets/main.js").strip()
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <!-- Nur Jimdos eigene Platzhalter im Kopf behalten; Styles kommen aus dem Reiter CSS (layout.css). -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <script>document.documentElement.classList.add('js')</script>
{indent(sprite, 2)}
  <a class="skip" href="#main">Zum Inhalt springen</a>

  <header class="nav jtpl-header" id="top">
    <div class="container nav__inner">
      <a href="/" class="brand" aria-label="Cafe Benjamico, zur Startseite">
        <svg class="brand__logo" viewBox="0 0 400 400" aria-hidden="true"><use href="#logo"/></svg>
        <span>Cafe <strong>Benjamico</strong></span>
      </a>
      <button class="nav__toggle" aria-expanded="false" aria-controls="menu" aria-label="Menü öffnen">
        <span></span><span></span>
      </button>
      <nav id="menu" class="nav__menu" aria-label="Hauptnavigation">
        <div class="jtpl-navigation navigation-colors">
          <var data-level="1">navigation</var>
        </div>
        <a class="btn btn--small" href="{RESERVATION}" target="_blank" rel="noopener">Tisch reservieren</a>
      </nav>
    </div>
  </header>

  <main id="main" class="jtpl-content content-options">
    <var>content</var>
  </main>

  <footer class="footer">
{indent(grid, 4)}
    <div class="container footer__bottom">
      <p>© <span id="year">2026</span> Cafe Benjamico</p>
      <div class="jtpl-footer footer-options">
        <var>footer</var>
      </div>
    </div>
  </footer>

  <script>
{indent(script, 2)}
  </script>
</body>
</html>
"""


def indent(text, n):
    return "\n".join((" " * n + l) if l else l for l in text.splitlines())


JIMDO_CSS = """
/* ==========================================================================
   Anpassungen für Jimdo Creator
   Jimdo erzeugt Navigation und Inhaltselemente selbst; hier werden sie an das
   Design der Website angeglichen.
   ========================================================================== */

/* Navigation: Jimdo liefert <ul class="cc-nav-level-0"><li><a> */
.jtpl-navigation ul { list-style: none; margin: 0; padding: 0; display: flex; align-items: center; gap: 6px; }
.jtpl-navigation li { margin: 0; padding: 0; background: none; }
.jtpl-navigation a { display: block; text-decoration: none; font-size: 1rem; font-weight: 500; color: var(--ink); padding: 8px 14px; border-radius: 999px; transition: background-color 200ms ease; }
.jtpl-navigation a:hover,
.jtpl-navigation .cc-nav-current > a,
.jtpl-navigation .cc-nav-parent > a { background: var(--tint); color: var(--ink); }

/* Inhalt: Widget/HTML-Bausteine laufen über die volle Breite, normale
   Jimdo-Elemente (Text, Überschrift, Bild, Formular …) bleiben lesbar schmal. */
.jtpl-content { display: block; min-height: 40vh; }
.jtpl-content .j-module { margin: 0; padding: 0; }
.jtpl-content .j-module:not(.j-htmlCode) { width: min(760px, 100% - 32px); margin: 0 auto 1.2rem; }
.jtpl-content .j-module:not(.j-htmlCode):first-child { margin-top: clamp(48px, 7vw, 96px); }
.jtpl-content .j-module:not(.j-htmlCode):last-child { margin-bottom: clamp(64px, 8vw, 112px); }
.jtpl-content .j-text p, .jtpl-content .j-text li { color: var(--muted); }
.jtpl-content .j-text a { color: var(--ink); text-decoration-color: var(--amber); text-underline-offset: 4px; }
.jtpl-content .j-imageSubtitle img, .jtpl-content .j-image img { border-radius: var(--r-media); }

/* Jimdo-Fußzeile (Impressum, Datenschutz, Sitemap, Anmelden) */
.jtpl-footer, .jtpl-footer a { color: var(--muted); font-size: .9rem; }
.jtpl-footer ul { list-style: none; display: flex; flex-wrap: wrap; gap: 4px 22px; margin: 0; padding: 0; }
.jtpl-footer li { margin: 0; }
.jtpl-footer a:hover { color: var(--ink); }

@media (max-width: 1080px) {
  .jtpl-navigation a { padding: 8px 10px; }
}
@media (max-width: 900px) {
  .jtpl-navigation ul { flex-direction: column; align-items: stretch; gap: 4px; }
  .jtpl-navigation a { padding: 12px 14px; font-size: 1.5rem; font-weight: 650; letter-spacing: -.02em; border-radius: 14px; }
}
"""


def css():
    style = read("assets/style.css")
    style = re.sub(r'url\("fonts/([\w.-]+)"\)', lambda m: f'url("{asset_url("assets/fonts/" + m.group(1))}")', style)
    head = "/* Cafe Benjamico – Layout-CSS für Jimdo Creator. Erzeugt von tools/build_jimdo.py aus assets/style.css. */\n"
    return head + style.rstrip() + "\n" + JIMDO_CSS


def head_html():
    index = read("index.html")
    ld = re.search(r'<script type="application/ld\+json">.*?</script>', index, re.S).group(0)
    fonts = "\n".join(
        f'<link rel="preload" href="{asset_url(a)}" as="font" type="font/woff2" crossorigin>'
        for a in ASSETS if a.endswith(".woff2"))
    return f"""<!-- Cafe Benjamico – Head-Code für Jimdo (Einstellungen > Head bearbeiten > ganze Website). -->
<meta name="theme-color" content="#f0f0e8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111814" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
{fonts}
{dedent(ld)}
"""


def main():
    FILES.update(load_files())
    (OUT / "seiten").mkdir(parents=True, exist_ok=True)
    (OUT / "layout.html").write_text(rewrite(layout()), encoding="utf-8")
    (OUT / "layout.css").write_text(css(), encoding="utf-8")
    (OUT / "head.html").write_text(head_html(), encoding="utf-8")
    for name in PAGES:
        (OUT / "seiten" / name).write_text(rewrite(page_snippet(name)), encoding="utf-8")
    print(f"Jimdo-Bausteine in {OUT.relative_to(ROOT)}/ erzeugt.")
    if MISSING:
        print(f"Hinweis: {len(MISSING)} Dateien haben noch keine Jimdo-Adresse (jimdo/dateien.json):")
        for p in sorted(MISSING):
            print("  -", p)


if __name__ == "__main__":
    main()
