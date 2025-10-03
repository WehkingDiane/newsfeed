import requests
import json
import datetime
import os

url = "https://www.tagesschau.de/api2u/news/"
params = {"ressort": "wirtschaft"}

def load_api_data(url, params):
    # Lade Daten von der Tagesschau API
    print("Lade Daten von Tagesschau API...")
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Fehler:", response.status_code)
    api_data = response.json()

    return api_data

def create_directory():
    # Verzeichnis für Ausgabe erstellen
    os.makedirs("Output", exist_ok=True)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    directory = os.path.join("Output", today)
    os.makedirs(directory, exist_ok=True)

    return directory

def save_api_data(directory, api_data):
    # Gesamte API-Daten speichern (zur Referenz)
    filename = os.path.join(directory, "tagesschau.json")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(api_data, indent=4, ensure_ascii=False))

def read_model_from_file(filepath):
    # JSON-Watchlist-Modell laden (z. B. news_watchlist_de.json).
    filepath = os.path.join("Model", filepath)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Fehler beim Lesen der Datei {filepath}: {e}")
        return None

def search_news(api_data, keyword):
    # Suche in API-Daten nach einem Stichwort und liefere Treffer.
    news_list = api_data.get("news", []) or api_data.get("items", [])
    results = []
    for news in news_list:
        tags = [t.get("tag", "").lower() for t in news.get("tags", [])]
        if keyword.lower() in tags:
            results.append(news)
    return results

api_data = load_api_data(url, params)
directory = create_directory()
save_api_data(directory, api_data)

# Watchlist laden (z. B. deutsche Keywords)
model_data = read_model_from_file("news_watchlist_de.json")
watchlist = model_data.get("watchlist", {})

# Ergebnisse sammeln
summary = {}

# Verarbeitung pro Aktie
for stock, categories in watchlist.items():
    print(f"Scanning {stock} ...")
    stock_results = {}
    total_hits = 0

    for category, content in categories.items():
        keywords = content.get("keywords", [])
        category_results = []

        for keyword in keywords:
            results = search_news(api_data, keyword)
            if results:
                category_results.extend(results)
                total_hits += len(results)

        if category_results:
            stock_results[category] = category_results

    # JSON-Datei pro Aktie speichern
    if stock_results:
        filename = os.path.join(directory, f"tagesschau_{stock}.json")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(stock_results, indent=4, ensure_ascii=False))

    summary[stock] = total_hits

# Zusammenfassung
print("\nZusammenfassung:")
for stock, hits in summary.items():
    print(f"- {stock}: {hits} Treffer")






