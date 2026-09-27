"""Erzeugt speisekarte.html aus tools/menu_data.py.

Preise/Gerichte in menu_data.py ändern, dann im Projektordner ausführen:
    python3 tools/build_speisekarte.py
Kopf, Menü und Fußzeile werden aus impressum.html übernommen.
"""
import html
import re
from pathlib import Path

import menu_data as M

ROOT = Path(__file__).resolve().parent.parent
e = html.escape

VEG = '<span class="tag tag--veg" title="vegetarisch">vegetarisch</span>'
VEGAN = '<span class="tag tag--vegan" title="vegan">vegan</span>'
NEW = '<span class="tag tag--new">Neu</span>'
TAGS = {"veg": VEG, "vegan": VEGAN, "vegan-option": '<span class="tag tag--vegan">auch vegan</span>'}


def dish(d):
    tags = TAGS.get(d.get("tag"), "") + (NEW if d.get("new") else "")
    extra = "".join(f"<li>{e(x)}</li>" for x in d.get("extra", []))
    sig = ""
    cls = "dish"
    if d.get("signature"):
        cls += " dish--signature"
        sig = ('<p class="dish__sig">Cafe Benjamico Signature ♥</p>'
               '<p class="dish__claim">Salzig, süß und unwiderstehlich. Probieren Sie es aus und lassen Sie sich '
               'von unserem Signature Dish überzeugen.</p>')
    return f'''          <article class="{cls}">
            <header class="dish__head"><h4>{e(d["name"])}</h4><span class="dish__price">{d["price"]}&nbsp;€</span></header>
            {sig}<p class="dish__desc">{e(d["desc"])}</p>
            <p class="dish__meta">{tags}<span class="allergens" title="Allergene">({e(d["allergens"])})</span></p>
            {f'<ul class="dish__extra">{extra}</ul>' if extra else ''}
          </article>
'''


def section(id_, script, title, note, dishes, after=""):
    return f'''    <section class="menu-section" id="{id_}">
      <div class="container">
        <header class="menu-section__head reveal">
          <p class="menu-script">{script}</p>
          <h2>{title}</h2>
          <p class="menu-note">{note}</p>
        </header>
        <div class="dishes reveal">
{"".join(dish(d) for d in dishes)}        </div>
{after}      </div>
    </section>
'''


def pricelist(rows):
    out = []
    for name, sub, price in rows:
        new = NEW if sub == "new" else ""
        sub_html = f'<small>{e(sub)}</small>' if sub and sub != "new" else ""
        out.append(f'<li><span class="pl__name">{e(name)}{new}{sub_html}</span><span class="pl__dots"></span><span class="pl__price">{price}</span></li>')
    return "\n              ".join(out)


extras = pricelist([(n + (f" ({a})" if a else ""), "", p) for n, a, p in M.EXTRAS])
extras_box = f'''        <aside class="menu-box reveal">
          <h3>Sie möchten mehr?</h3>
          <ul class="pl pl--2col">
              {extras}
          </ul>
        </aside>
'''

drinks = ""
for title, rows, note in M.GETRAENKE:
    drinks += f'''          <div class="drink-group">
            <h3>{e(title)}</h3>
            <ul class="pl">
              {pricelist(rows)}
            </ul>
            {f'<p class="menu-note menu-note--small">{e(note)}</p>' if note else ''}
          </div>
'''
specials = "\n              ".join(
    f'<li><span class="pl__name">{e(n)}{" ♥" if fav else ""}{f"<small>{e(s)}</small>" if s else ""}</span><span class="pl__dots"></span><span class="pl__price">{p}</span></li>'
    for n, s, p, fav in M.SPECIALS)

allergene = " · ".join(f"<b>{k}</b> {e(v)}" for k, v in M.ALLERGENE)

body = f'''  <main id="main">
    <section class="page-hero page-hero--menu">
      <div class="container menu-intro reveal">
        <p class="eyebrow">Mit Liebe. Mit Qualität. Für Sie.</p>
        <h1>Mehr als nur ein Cafe.<br><em>Ein Ort zum Ankommen.</em></h1>
        <p class="lead">Bei uns dreht sich alles um guten Geschmack, ehrliche Zutaten und herzliche Begegnungen. Egal ob Sie den Tag mit einem ausgiebigen Frühstück beginnen, mit Freunden ein Glas Wein trinken oder einfach eine kleine Auszeit genießen möchten – wir freuen uns, dass Sie hier sind.</p>
      </div>
    </section>

    <nav class="menu-tabs" aria-label="Speisekarte">
      <div class="container menu-tabs__inner">
        <a href="#fruehstueck">Frühstück</a>
        <a href="#bagels">Bagels &amp; Stullen</a>
        <a href="#sweet">Sweet Stuff</a>
        <a href="#lunch">Lunch</a>
        <a href="#getraenke">Getränke</a>
      </div>
    </nav>

{section("fruehstueck", "Breakfast all day long", "Frühstück", "Frühstück und warme Küche bis 16:00 Uhr", M.FRUEHSTUECK, extras_box)}
{section("bagels", "Bagels &amp; Stullen", "Bagels und Stullen", "Mit Brot von Brot &amp; Sinne", M.BAGELS)}
{section("sweet", "Sweet Stuff", "Süßes Frühstück", "Frühstück und warme Küche bis 16:00 Uhr", M.SWEET)}
{section("lunch", "Lunch", "Mittagstisch", "Lunch ab 11:30 Uhr", M.LUNCH)}
    <section class="menu-section menu-section--drinks" id="getraenke">
      <div class="container">
        <header class="menu-section__head reveal">
          <p class="menu-script">Getränke &amp; Specials</p>
          <h2>Getränke</h2>
        </header>
        <div class="drinks reveal">
{drinks}        </div>
        <aside class="menu-box menu-box--specials reveal">
          <h3>Specials</h3>
          <ul class="pl">
              {specials}
          </ul>
        </aside>
      </div>
    </section>

    <section class="section section--tint">
      <div class="container duo">
        <article class="panel reveal">
          <p class="eyebrow">Unsere Philosophie</p>
          <h2>Für Sie. Für uns. Für morgen.</h2>
          <p>Wir glauben an ehrliche Lebensmittel, die mit Sorgfalt ausgewählt und mit Liebe zubereitet werden. Regionalität, Nachhaltigkeit und Qualität stehen für uns an erster Stelle – für einen guten Geschmack und ein gutes Gefühl.</p>
        </article>
        <article class="panel reveal">
          <p class="eyebrow">Unsere Lieferanten</p>
          <h2>Regional &amp; mit Leidenschaft</h2>
          <p>Wir arbeiten mit regionalen Partnern und Manufakturen zusammen, die unsere Werte teilen und mit Leidenschaft hervorragende Produkte herstellen. So zum Beispiel:</p>
          <ul class="chips">
            <li>Brot und Sinne</li>
            <li>Geflügelhof Zenner</li>
            <li>Bruch Brauerei</li>
            <li>Black Hen Rösterei</li>
          </ul>
        </article>
      </div>
      <div class="container">
        <div class="info-strip reveal">
          <p><strong>Kartenzahlung?</strong> Sehr gerne.</p>
          <p><strong>Trinkgeld auch per Karte möglich.</strong> 100&nbsp;% des Trinkgelds gehen an unser Team und werden fair unter den Mitarbeitenden aufgeteilt – egal ob bar oder mit Karte.</p>
        </div>
        <p class="allergen-legend reveal"><span class="tag tag--veg">vegetarisch</span> <span class="tag tag--vegan">vegan</span><br><b>Allergene:</b> {allergene}</p>
      </div>
    </section>
  </main>

'''

tpl = (ROOT / "impressum.html").read_text()
head = tpl[:tpl.index('  <main id="main"')]
foot = tpl[tpl.index('  <footer class="footer">'):]
head = head.replace("<title>Impressum – Cafe Benjamico</title>", "<title>Speisekarte – Cafe Benjamico</title>")
head = re.sub(r'<meta name="description" content="[^"]*">\n  <meta name="robots" content="noindex">',
              '<meta name="description" content="Speisekarte des Cafe Benjamico in Riegelsberg: Frühstück den ganzen Tag, Bagels &amp; Stullen, French Toast, saisonaler Lunch, Kaffeespezialitäten und Getränke – auch vegetarisch und vegan.">', head)
head = head.replace('<a href="impressum.html" aria-current="page">', '<a href="impressum.html">')
head = head.replace('<a href="speisekarte.html">Speisekarte</a>', '<a href="speisekarte.html" aria-current="page">Speisekarte</a>')
(ROOT / "speisekarte.html").write_text(head + body + foot)
print("speisekarte.html geschrieben")
