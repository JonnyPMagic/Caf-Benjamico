# Cafe Benjamico – Website

Statische Website (HTML/CSS/JS, kein Build-System nötig) für das Cafe Benjamico in Riegelsberg-Walpershofen.

## Seiten

| Datei | Menüpunkt |
| --- | --- |
| `index.html` | Startseite |
| `speisekarte.html` | Speisekarte (wird erzeugt, siehe unten) |
| `angebot.html` | Unser Angebot |
| `trauerfeiern.html` | Trauerfeiern |
| `feiern.html` | Private Feiern |
| `impressum.html`, `datenschutz.html` | Rechtliches (Fußzeile) |

Gemeinsame Gestaltung: `assets/style.css`, Verhalten (Menü, Öffnungsstatus, Formular, Speisekarten-Navigation): `assets/main.js`.

## Speisekarte ändern

Gerichte, Preise und Allergene stehen in `tools/menu_data.py`. Nach einer Änderung:

```sh
python3 tools/build_speisekarte.py
```

Das erzeugt `speisekarte.html` neu (Kopf, Menü und Fußzeile werden aus `impressum.html` übernommen). Für Jimdo danach auch `python3 tools/build_jimdo.py` ausführen.

## Auf Jimdo nutzen

Die Website lässt sich zusätzlich als eigenes Layout in **Jimdo Creator** betreiben. Die Bausteine dafür erzeugt:

```sh
python3 tools/build_jimdo.py
```

Ergebnis und Schritt-für-Schritt-Anleitung: `jimdo/ANLEITUNG.md`.

## Lokal ansehen

```sh
python3 -m http.server 8000
# dann http://localhost:8000 öffnen
```
