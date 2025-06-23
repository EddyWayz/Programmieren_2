# Programmieren 2 – C/C++ Lernmaterial

Dieses Repository enthält HTML-Präsentationen und Übungsunterlagen für die Vorlesung *Programmieren 2*. Die Kapitel vermitteln Schritt für Schritt die Grundlagen der Programmiersprachen **C** und **C++**.

## Projektstruktur
- `index.html` – Startseite mit Links zu allen Kapiteln
- `c/` und `cpp/` – HTML-Slides für C bzw. C++
- `material/` – PDF-Skripte und Übungsblätter (siehe unten)
- `style.css` – gemeinsames Layout

## Lokales Öffnen von `index.html`
Die einfachste Variante ist, `index.html` im Browser zu öffnen (Doppelklick oder per `Datei > Öffnen`). Alternativ lässt sich ein lokaler HTTP-Server nutzen:

```bash
# Python 3
python3 -m http.server
```

Anschließend kann `http://localhost:8000/index.html` im Browser aufgerufen werden. In Visual Studio Code bietet sich auch die Erweiterung *Live Server* (Port 5501) an.

## Materialien (`material/`)
Im Ordner `material/` befinden sich ausführliche Skripte zu jeder Vorlesungseinheit sowie Übungsaufgaben für **C** und **C++**. Zum Betrachten wird lediglich ein PDF-Reader benötigt. Für die praktischen Aufgaben sollte eine aktuelle C/C++-Entwicklungsumgebung (z.B. GCC oder clang) installiert sein.

## Optionale Werkzeuge
Um die HTML-Dateien komfortabel zu nutzen, kann ein lokaler Webserver hilfreich sein. Unter Python steht `http.server` standardmäßig zur Verfügung. Unter Node.js eignet sich das Paket `http-server`:

```bash
npm install -g http-server
http-server -p 8000
```

Das Repository enthält keine Abhängigkeiten und benötigt auch keine Build-Schritte.

## Lizenz
Der Inhalt dieses Repositories steht unter der [MIT-Lizenz](LICENSE).
