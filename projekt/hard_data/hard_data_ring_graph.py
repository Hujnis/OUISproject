import json
import plotly.graph_objects as go

# Cesty k souborům
input_json_path = 'C:/Users/thujn/OUISproject/projekt/hard_data/hard_data.json'


# Načtení JSON dat ze souboru
with open(input_json_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Extrakce dat z JSON
events = json_data['data']['eventPage']

# Příprava dat pro analýzu
groups = {}
places = {}
event_names = {}
event_types = {}

for event in events:
    for group in event['groups']:
        group_name = group['name']
        if group_name not in groups:
            groups[group_name] = {
                'places': {},
                'event_names': {},
                'event_types': {}
            }
        
        place_name = event['place']
        event_name = event['name']
        event_type = event['eventType']['name']
        
        groups[group_name]['places'][place_name] = groups[group_name]['places'].get(place_name, 0) + 1
        groups[group_name]['event_names'][event_name] = groups[group_name]['event_names'].get(event_name, 0) + 1
        groups[group_name]['event_types'][event_type] = groups[group_name]['event_types'].get(event_type, 0) + 1

# Vytvoření vícevrstvého prstencového grafu pro každou skupinu
fig = go.Figure()

for group_name, data in groups.items():
    # Střední vrstva - místa
    fig.add_trace(go.Pie(
        labels=list(data['places'].keys()),
        values=list(data['places'].values()),
        name=group_name,
        hole=0.1,
        textposition='auto',
        textinfo='label',
        hoverinfo='label+percent',
        textfont=dict(size=9),  # Nastavení velikosti písma
        marker=dict(line=dict(color='#000000', width=1))
    ))

    # Vnější vrstva - události
    fig.add_trace(go.Pie(
        labels=list(data['event_names'].keys()),
        values=list(data['event_names'].values()),
        name=group_name,
        hole=0.4,
        textposition='auto',
        textinfo='label',
        hoverinfo='label+percent',
        textfont=dict(size=9),  # Nastavení velikosti písma
        marker=dict(line=dict(color='#000000', width=1))
    ))

    # Vnější vnější vrstva - typy událostí
    fig.add_trace(go.Pie(
        labels=list(data['event_types'].keys()),
        values=list(data['event_types'].values()),
        name=group_name,
        hole=0.8,
        textposition='auto',
        textinfo='label',
        hoverinfo='label+percent',
        textfont=dict(size=10),  # Nastavení velikosti písma
        marker=dict(line=dict(color='#000000', width=1))
    ))

# Nastavení středového textu
fig.update_layout(
    annotations=[dict(text=group_name, x=0.5, y=0.5, font_size=13, showarrow=False) for group_name in groups],
    showlegend=False
)

# Nastavení velikosti grafu
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(t=50, b=50, l=50, r=50)
)

# Zobrazení grafu
fig.show()
