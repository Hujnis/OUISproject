import pandas as pd
import json
from tabulate import tabulate

# Načtení dat ze souboru data.json
with open('C:/Users/thujn/OUISproject/projekt/data.json', 'r') as file:
    data = json.load(file)

# Vytvoření pandas DataFrame z eventPage
df = pd.DataFrame(data['data']['eventPage'])

# Přejmenování sloupců pro lepší čitelnost
df.columns = ['id', 'name', 'place', 'startdate', 'enddate']

# Převedení DataFrame na list slovníků
data_list = df.to_dict(orient='records')

# Uložení kontingenční tabulky do souboru JSON
with open('C:/Users/thujn/OUISproject/projekt/contingency_table2.json', 'w') as file:
    json.dump(data_list, file, indent=4)

print("Kontingenční tabulka byla uložena do souboru 'contingency_table2.json'.")
