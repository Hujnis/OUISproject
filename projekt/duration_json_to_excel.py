import json
import pandas as pd

# Cesta k vstupnímu souboru
input_file_path = "C:/Users/thujn/OUISproject/projekt/duration_results.json"
# Cesta k výstupnímu Excel souboru
output_file_path = "C:/Users/thujn/OUISproject/projekt/excel_table_duration.xlsx"

# Načtení dat ze vstupního souboru
with open(input_file_path, 'r', encoding='utf-8') as file:
    data_dict = json.load(file)

# Převod dat do DataFrame
data_list = [{"Event-Group": k, "Duration": v} for k, v in data_dict.items()]
df = pd.DataFrame(data_list)

# Rozdělení sloupce "Event-Group" na "Event" a "Group"
df[['Event', 'Group']] = df['Event-Group'].str.split(' - ', expand=True)
df.drop(columns=['Event-Group'], inplace=True)

# Uložení DataFrame do Excel souboru
df.to_excel(output_file_path, index=False)

print("Data byla úspěšně převedena a uložena do Excel souboru.")

