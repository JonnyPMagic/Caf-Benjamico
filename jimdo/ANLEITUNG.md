# Cafe Benjamico auf Jimdo Creator

In diesem Ordner liegt die Website als Bausteine für **Jimdo Creator**. Das Design steckt in einem eigenen Layout. Seiten, Navigation, Impressum und Datenschutz verwaltest du weiter ganz normal im Jimdo-Editor.

> Für ein eigenes Layout braucht Jimdo Creator das Paket **Pro** oder **Business**. Bei „Head bearbeiten“ ist es genauso.

Alle Dateien hier werden automatisch aus der normalen Website erzeugt. Nach Änderungen an der Website (oder an `dateien.json`):

```sh
python3 tools/build_jimdo.py
```

| Datei | Wohin bei Jimdo |
| --- | --- |
| `layout.html` | Design → Layout → Eigenes Layout bearbeiten → Reiter **HTML** |
| `layout.css` | Design → Layout → Eigenes Layout bearbeiten → Reiter **CSS** |
| `head.html` | Einstellungen → Head bearbeiten → **ganze Website** |
| `seiten/*.html` | je Seite in ein Element **Widget/HTML** |
| `dateien.json` | Adressen der hochgeladenen Bilder und Schriften (s. Schritt 1) |

## 1. Bilder und Schriften hochladen

Jimdo kann keine ganzen Ordner hosten. Deshalb lädst du die Dateien aus `assets/img/` und `assets/fonts/` einzeln hoch, am besten im Layout-Editor unter **Dateien**. Kopiere zu jeder Datei die Adresse, die Jimdo anzeigt, und trag sie in `jimdo/dateien.json` ein:

```json
"assets/img/innenraum-800.webp": "https://…jimdo…/innenraum-800.webp",
```

Liegen alle Dateien unter einer gemeinsamen Adresse (z. B. auf einem eigenen Webspace), reicht `"_basis": "https://beispiel.de"`.

Danach `python3 tools/build_jimdo.py` ausführen. Das Skript meldet, welche Dateien noch keine Adresse haben.

## 2. Layout einrichten

1. Design → Layout → **Eigenes Layout** (bzw. „Layout bearbeiten“) öffnen.
2. Reiter **HTML**: den Inhalt komplett durch `layout.html` ersetzen. Stehen in Jimdos Vorlage im `<head>` eigene Platzhalter, lass diese stehen und übernimm nur den Teil ab `<body>`.
3. Reiter **CSS**: den Inhalt komplett durch `layout.css` ersetzen.
4. Speichern. Unter **Design → Stil** am besten nichts einstellen, sonst überschreibt Jimdo Farben und Schriften des Layouts.

Das Layout nutzt Jimdos Platzhalter:

- `<var data-level="1">navigation</var>`: die Hauptnavigation, gepflegt unter „Navigation bearbeiten“
- `<var>content</var>`: der Seiteninhalt
- `<var>footer</var>`: Jimdos Pflicht-Fußzeile mit Impressum, Datenschutz, Sitemap und Anmelden

Der Knopf „Tisch reservieren“, das Logo und die Fußzeile mit Öffnungszeiten und Kontakt stehen fest im Layout (`layout.html`).

## 3. Seiten anlegen

Unter „Navigation bearbeiten“ diese Seiten anlegen, in genau dieser Schreibweise. Jimdo bildet daraus die Adressen, auf die die internen Links zeigen:

| Seitenname | Adresse | Baustein |
| --- | --- | --- |
| Startseite | `/` | `seiten/index.html` |
| Speisekarte | `/speisekarte/` | `seiten/speisekarte.html` |
| Unser Angebot | `/unser-angebot/` | `seiten/angebot.html` |
| Trauerfeiern | `/trauerfeiern/` | `seiten/trauerfeiern.html` |
| Private Feiern | `/private-feiern/` | `seiten/feiern.html` |

Auf jeder Seite alle alten Elemente löschen, ein Element **Widget/HTML** einfügen und den Inhalt der passenden Datei hineinkopieren.

Heißt eine Seite bei dir anders, trag die Adresse oben in `tools/build_jimdo.py` (`PAGES`) ein und erzeuge die Bausteine neu.

## 4. Impressum, Datenschutz und Kopfbereich

- **Impressum** und **Datenschutz** sind bei Jimdo feste Systemseiten (Links in der Fußzeile). Übernimm die Texte aus `seiten/impressum.html` und `seiten/datenschutz.html` in Jimdos Impressum- bzw. Datenschutz-Einstellungen.
- **Seitentitel und Beschreibung** (für Google) pro Seite unter Einstellungen → SEO eintragen, die Texte stehen jeweils im `<title>` und `<meta name="description">` der HTML-Dateien im Hauptordner.
- **Favicon**: `assets/favicon.svg` unter Einstellungen → Favicon hochladen (Jimdo verlangt ggf. PNG/ICO).
- **head.html** unter Einstellungen → Head bearbeiten → ganze Website einfügen: Farbschema, vorgeladene Schriften und die Café-Daten für Google (Öffnungszeiten, Adresse).

## Inhalte ändern

- **Speisekarte**: `tools/menu_data.py` ändern, dann `python3 tools/build_speisekarte.py` und `python3 tools/build_jimdo.py`, anschließend `seiten/speisekarte.html` erneut ins Widget kopieren.
- **Kleine Textänderungen** kannst du auch direkt im Widget bei Jimdo machen. Dann weichen Jimdo und die Dateien hier aber voneinander ab. Besser: in der HTML-Datei im Hauptordner ändern und neu erzeugen.
- **Eigene Jimdo-Elemente** (Text, Bild, Formular …) funktionieren weiterhin. Das Layout stellt sie in einer schmalen, gut lesbaren Spalte im Stil der Website dar.
