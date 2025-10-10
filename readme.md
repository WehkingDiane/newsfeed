# Tagesschau Newsfeed

Dieses Projekt sammelt und analysiert aktuelle Nachrichten der Tagesschau und stellt sie sortiert nach Unternehmen und Branchen dar. Die News werden gefiltert und in einer Watchlist nach relevanten Stichworten gruppiert. Die Ergebnisse werden als JSON-Dateien gespeichert und können über eine Streamlit-Weboberfläche angezeigt werden.

## Start Befehle

### 1. Nachrichten abrufen und speichern
```
python .\tagesschau.py
```
Dieses Skript lädt die aktuellen News und speichert sie im Output-Ordner als JSON-Dateien.

### 2. Web-App starten (News anzeigen)
```
streamlit run main.py
```
Damit wird die Streamlit-Oberfläche geöffnet, in der die News sortiert und gefiltert angezeigt werden.

## Voraussetzungen

- Python 3.x
- Die Pakete aus `requirements.txt` müssen installiert sein (z.B. mit `pip install -r requirements.txt`).

## Ordnerstruktur

- `Output/` – Hier werden die News-Dateien abgelegt.
- `Model/news_watchlist_de.json` – Enthält die Watchlist mit relevanten Stichworten.
- `main.py` – Streamlit Web-App zur Anzeige der News.
- `tagesschau.py` – Skript zum Abrufen und Speichern der Nachrichten.