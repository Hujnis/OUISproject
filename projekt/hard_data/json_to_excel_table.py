import json
import pandas as pd
from datetime import datetime

# Cesty ke vstupnímu JSON souboru a výstupnímu Excel souboru
input_json_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/hard_data.json'
output_excel_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/hard_data_excel_table.xlsx'

# Funkce pro výpočet délky trvání
def calculate_duration(start, end):
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    duration = end_dt - start_dt
    return duration

# Načtení JSON dat ze souboru
with open(input_json_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Extrahování relevantních dat z JSON
events = json_data['data']['eventPage']

# Převod dat na strukturu vhodnou pro pandas DataFrame
data = []
for event in events:
    for group in event['groups']:
        duration = calculate_duration(event['startdate'], event['enddate'])
        data.append({
            'name': event['name'],
            'place': event['place'],
            'startdate': event['startdate'],
            'enddate': event['enddate'],
            'duration': str(duration),  # Přidání trvání jako string
            'eventType': event['eventType']['name'],
            'group_id': group['id'],
            'group_name': group['name']
        })

# Vytvoření pandas DataFrame
df = pd.DataFrame(data)

# Uložení DataFrame do Excel souboru
df.to_excel(output_excel_path, index=False, engine='openpyxl')

print(f"Data byla úspěšně převedena do souboru {output_excel_path}")


