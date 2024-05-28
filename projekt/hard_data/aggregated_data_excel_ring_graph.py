import json
from collections import defaultdict
import pandas as pd
import plotly.graph_objects as go

# Cesty k souborům
input_json_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/hard_data.json'
output_excel_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/aggregated_data.xlsx'

# Načtení JSON dat ze souboru
with open(input_json_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Extrakce dat z JSON
events = json_data['data']['eventPage']

# Agregace dat pro prstencový graf
aggregated_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

for event in events:
    group_name = event["groups"][0]["name"]
    place = event["place"]
    event_name = event["name"]
    
    aggregated_data[group_name][place][event_name].append(event_name)

# Vykreslení prstencového grafu
fig = go.Figure()

# Nastavení barev pro jednotlivé vrstvy
colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5', '#392F5A', '#31A2AC', '#61C0BF']

# Přidání vrstev do grafu
layer1_labels = []
layer1_values = []
layer1_parents = []

layer2_labels = []
layer2_values = []
layer2_parents = []

layer3_labels = []
layer3_values = []
layer3_parents = []

# Procházení agregovaných dat a naplnění jednotlivých vrstev
for group, places in aggregated_data.items():
    group_events_count = sum(len(event_types) for events in places.values() for event_types in events.values())
    layer1_labels.append(group)
    layer1_values.append(group_events_count)
    layer1_parents.append("")
    
    for place, events in places.items():
        place_events_count = sum(len(event_types) for event_types in events.values())
        layer2_labels.append(place)
        layer2_values.append(place_events_count)
        layer2_parents.append(group)
        
        for event_name, event_types in events.items():
            layer3_labels.append(event_name)
            layer3_values.append(len(event_types))
            layer3_parents.append(place)

# Vytvoření jednotlivých vrstev grafu
labels = layer1_labels + layer2_labels + layer3_labels
values = layer1_values + layer2_values + layer3_values
parents = layer1_parents + layer2_parents + layer3_parents

# Vytvoření hovertemplate pro zobrazení procentuálního výskytu
total_value = sum(values)
hover_template = '%{label}: %{value} (%{percentParent:.1%}, %{percentEntry:.1%} celkem)'

fig.add_trace(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",
    marker=dict(colors=colors),
    maxdepth=3,  # Maxdepth 3, protože máme tři vrstvy
    hovertemplate=hover_template
))

# Nastavení vzhledu grafu
fig.update_layout(
    margin=dict(t=0, l=0, r=0, b=0),
    sunburstcolorway=colors,
    title="Vícevrstvý prstencový graf událostí"
)

# Zobrazení grafu
fig.show()

# Agregace dat pro Excel
aggregated_data_excel = {}

for event in events:
    group_name = event["groups"][0]["name"]
    place = event["place"]
    event_name = event["name"]
    
    if group_name not in aggregated_data_excel:
        aggregated_data_excel[group_name] = {}
    if place not in aggregated_data_excel[group_name]:
        aggregated_data_excel[group_name][place] = []
    
    aggregated_data_excel[group_name][place].append(event_name)

# Vytvoření seznamu řádků pro DataFrame pro Excel
rows_excel = []

for group, places in aggregated_data_excel.items():
    for place, events in places.items():
        for event in events:
            rows_excel.append({'Group': group, 'Place': place, 'Event': event})

# Vytvoření DataFrame z agregovaných dat pro Excel
df_excel = pd.DataFrame(rows_excel)

# Uložení do Excelu
df_excel.to_excel(output_excel_path, index=False)

print(f"Agregovaná data byla uložena do souboru: {output_excel_path}")
