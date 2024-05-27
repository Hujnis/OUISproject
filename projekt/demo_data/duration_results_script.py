import json
from datetime import datetime

# Cesta k vstupnímu a výstupnímu souboru
input_file_path = "C:/Users/thujn/OUISproject/projekt/demo_data/data.json"
output_file_path = "C:/Users/thujn/OUISproject/projekt/demo_data/duration_results.json"

# Načtení dat ze vstupního souboru
with open(input_file_path, 'r', encoding='utf-8') as file:
    data_dict = json.load(file)

# Dictionary pro ukládání doby trvání pro každou kombinaci groups a name
duration_dict = {}

# Projdeme všechny události
for event in data_dict['data']['eventPage']:
    # Získáme název události
    event_name = event['name']
    
    # Získáme datum zahájení a ukončení
    start_date = datetime.fromisoformat(event['startdate'])
    end_date = datetime.fromisoformat(event['enddate'])
    
    # Vypočteme dobu trvání
    duration = end_date - start_date
    
    # Projdeme všechny skupiny
    for group in event['groups']:
        group_name = group['name']
        # Vytvoříme klíč pro kombinaci názvu události a názvu skupiny
        key = f"{event_name} - {group_name}"
        # Uložíme dobu trvání do slovníku
        duration_dict[key] = str(duration)

# Uložení výsledků do výstupního souboru
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(duration_dict, output_file, indent=4, ensure_ascii=False)

print("Výsledky byly úspěšně uloženy do souboru.")
