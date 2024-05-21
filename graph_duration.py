import json
import pandas as pd
import matplotlib.pyplot as plt

# Cesta k vstupnímu souboru
input_file_path = "C:/Users/thujn/OUISproject/projekt/duration_results.json"

# Načtení dat ze vstupního souboru
with open(input_file_path, 'r', encoding='utf-8') as file:
    data_dict = json.load(file)

# Převod dat do DataFrame
data_list = [{"Event-Group": k, "Duration": v} for k, v in data_dict.items()]
df = pd.DataFrame(data_list)

# Rozdělení sloupce "Event-Group" na "Event" a "Group"
df[['Event', 'Group']] = df['Event-Group'].str.split(' - ', expand=True)
df.drop(columns=['Event-Group'], inplace=True)

# Převod sloupce Duration na časový formát
df['Duration'] = pd.to_timedelta(df['Duration'])

# Příprava dat pro graf
groups = df['Group'].tolist()
durations = df['Duration'].dt.total_seconds() / 3600  # Doba trvání v hodinách

# Vytvoření vícevrstvého prstencového grafu
fig, ax = plt.subplots()

# Druhá vrstva - groups
size = 0.3
group_counts = [1] * len(groups)  # Počet skupin (každá skupina má stejnou váhu)
ax.pie(group_counts, labels=groups, radius=1, wedgeprops=dict(width=size, edgecolor='w'))

# Třetí vrstva - durations
ax.pie(durations, labels=durations.astype(str) + ' h', radius=1 + size, wedgeprops=dict(width=size, edgecolor='w'))

# Text ve středu - Zkouška
ax.text(0, 0, 'Zkouška', horizontalalignment='center', verticalalignment='center', fontsize=20, color='black')

# Zobrazení grafu
plt.title('Vícevrstvý prstencový graf: Skupiny a Duration')
plt.show()
