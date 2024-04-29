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

# Uložení kontingenční tabulky do souboru
with open('C:/Users/thujn/OUISproject/projekt/contingency_table.json', 'w') as file:
    file.write(tabulate(df, headers='keys', tablefmt='pipe', showindex=False))

print("Kontingenční tabulka byla uložena do souboru 'contingency_table.json'.")
