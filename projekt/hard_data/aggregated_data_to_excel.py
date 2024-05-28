import json
import pandas as pd

# Cesta k souboru s JSON daty
input_json_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/hard_data.json'
output_excel_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/aggregated_data.xlsx'

# Načtení JSON dat ze souboru
with open(input_json_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Extrakce dat z JSON
events = json_data['data']['eventPage']

# Agregace dat
aggregated_data = {}

for event in events:
    group_name = event["groups"][0]["name"]
    place = event["place"]
    event_name = event["name"]
    
    if group_name not in aggregated_data:
        aggregated_data[group_name] = {}
    if place not in aggregated_data[group_name]:
        aggregated_data[group_name][place] = []
    
    aggregated_data[group_name][place].append(event_name)

# Vytvoření seznamu řádků pro DataFrame
rows = []

for group, places in aggregated_data.items():
    for place, events in places.items():
        for event in events:
            rows.append({'Group': group, 'Place': place, 'Event': event})

# Vytvoření DataFrame z agregovaných dat
df = pd.DataFrame(rows)

# Uložení do Excelu
df.to_excel(output_excel_path, index=False)

print(f"Agregovaná data byla uložena do souboru: {output_excel_path}")
