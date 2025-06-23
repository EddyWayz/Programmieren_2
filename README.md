# Programmieren 2 – C/C++ Lernmaterial

Dieses Repository enthält HTML-Präsentationen und Übungsunterlagen für die Vorlesung *Programmieren 2*. Die Kapitel vermitteln Schritt für Schritt die Grundlagen der Programmiersprachen **C** und **C++**. Im ersten Teil lernst du systematisch die Sprache **C**, im zweiten Teil erfolgt der Einstieg in moderne **C++**-Konzepte.

## Projektstruktur
- `index.html` – Startseite mit Links zu allen Kapiteln
- `c/` und `cpp/` – HTML-Slides für C bzw. C++
- `material/` – PDF-Skripte und Übungsblätter (siehe unten)
- `examples/` – kleine Programme zum Nachprogrammieren
- `style.css` – gemeinsames Layout
- `tools/generate_index.py` – Skript zum Aktualisieren des Inhaltsverzeichnisses

## Lokales Öffnen von `index.html`
Die einfachste Variante ist, `index.html` im Browser zu öffnen (Doppelklick oder per `Datei > Öffnen`). Alternativ lässt sich ein lokaler HTTP-Server nutzen:

```bash
# Python 3
python3 -m http.server
```

Anschließend kann `http://localhost:8000/index.html` im Browser aufgerufen werden. In Visual Studio Code bietet sich auch die Erweiterung *Live Server* (Port 5501) an.

Neue Kapitel musst du lediglich im Ordner `c/` oder `cpp/` ablegen. Mit
`python3 tools/generate_index.py` wird anschließend das Inhaltsverzeichnis in
`index.html` automatisch aktualisiert.

## Materialien (`material/`)
Im Ordner `material/` befinden sich ausführliche Skripte zu jeder Vorlesungseinheit sowie Übungsaufgaben für **C** und **C++**. Zum Betrachten wird lediglich ein PDF-Reader benötigt. Für die praktischen Aufgaben sollte eine aktuelle C/C++-Entwicklungsumgebung (z.B. GCC oder clang) installiert sein.

## Optionale Werkzeuge
Um die HTML-Dateien komfortabel zu nutzen, kann ein lokaler Webserver hilfreich sein. Unter Python steht `http.server` standardmäßig zur Verfügung. Unter Node.js eignet sich das Paket `http-server`:

```bash
npm install -g http-server
http-server -p 8000
```

Das Repository enthält keine Abhängigkeiten und benötigt auch keine Build-Schritte.

## Hosting auf GitHub Pages
Wenn du die Slides online bereitstellen möchtest, kannst du GitHub Pages nutzen:

1. Lege einen Branch `gh-pages` an (z.B. mit `git switch --orphan gh-pages`).
2. Aktiviere unter den Repository-Einstellungen den Bereich **Pages** und wähle diesen Branch aus.
3. Nach wenigen Minuten sind die Dateien unter `https://<username>.github.io/<repository>` erreichbar.

## Lizenz
Der Inhalt dieses Repositories steht unter der [MIT-Lizenz](LICENSE).
