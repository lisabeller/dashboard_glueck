### World Happiness Dashboard

Ein interaktives Dashboard zur Visualisierung und Analyse des World Happiness Reports mit Daten bis 2024.

#### Beschreibung
Dieses Dashboard bietet eine umfassende Visualisierung der Glücklichkeitsdaten verschiedener Länder weltweit. Es ermöglicht die interaktive Exploration von Faktoren wie BIP pro Kopf, soziale Unterstützung und Lebenserwartung im Zusammenhang mit dem Glücklichkeitswert der Länder.

#### Hauptfunktionen
- Interaktive Weltkarte mit Glücklichkeitswerten
- Detaillierte Länderanalysen mit Liniendiagrammen
- Vergleichende Visualisierungen (Top 5, Top/Bottom 5)
- Korrelationsanalysen verschiedener Faktoren
- Informative Dashboards mit Schlüsselindikatoren
- #### Erforderliche Pakete
pandas
plotly.express
dash
func_plots (eigenes Modul)

#### Datenquellen
whr-2024.csv
DataForFigure2.1+with+sub+bars+2024.csv
infobox.csv

#### Verwendung
Starten Sie die Anwendung:
bash
Copy Code
python app.py
Öffnen Sie einen Webbrowser und navigieren Sie zu:
http://localhost:8050

#### Funktionen im Detail
Infoboard: Klickbare Kacheln mit detaillierten Informationen
Weltkarte: Interaktive Visualisierung der globalen Glücklichkeitswerte
Länderanalyse: Detaillierte Informationen und Trends für einzelne Länder
Vergleichende Analysen:
BIP vs. Glücklichkeitswert
Entscheidungsfreiheit vs. Positiver Effekt
Top 5 Länder-Rankings
Top/Bottom 5 Vergleiche

#### Entwicklerinnen
Lisa Beller
Karin Wiedemann

Hinweise
Die Anwendung verwendet den Debug-Modus für die Entwicklung
Alle Visualisierungen sind interaktiv und ermöglichen Zoom/Pan


#### Installation
1. Klonen Sie das Repository:
```bash
git clone [repository-url]

2. Installieren Sie die erforderlichen Pakete:
bash
Copy Code
pip install -r requirements.txt

#### Erforderliche Pakete
pandas
plotly.express
dash
func_plots (eigenes Modul)

#### Datenquellen
whr-2024.csv
DataForFigure2.1+with+sub+bars+2024.csv
infobox.csv

#### Verwendung
Starten Sie die Anwendung:
bash
Copy Code
python app.py
Öffnen Sie einen Webbrowser und navigieren Sie zu:
http://localhost:8050
Funktionen im Detail
Infoboard: Klickbare Kacheln mit detaillierten Informationen
Weltkarte: Interaktive Visualisierung der globalen Glücklichkeitswerte
Länderanalyse: Detaillierte Informationen und Trends für einzelne Länder
Vergleichende Analysen:
BIP vs. Glücklichkeitswert
Entscheidungsfreiheit vs. Positiver Effekt
Top 5 Länder-Rankings
Top/Bottom 5 Vergleiche
Entwickler
Lisa Beller
Karin Wiedemann
Lizenz
© DataCraft - 2024

Hinweise
Die Anwendung verwendet den Debug-Modus für die Entwicklung
Alle Visualisierungen sind interaktiv und ermöglichen Zoom/Pan
