import pandas as pd
import matplotlib.pyplot as plt
'''
# Loading data and adding a 'Year' column for each dataset
data_2018 = pd.read_csv('income-restricted-inventory-2018-all-income-restricted-projects.csv')
data_2018['Year'] = 2018  # Corrected to 2018 based on your file name
MIGHT be better to leave this out
'''

data_2020 = pd.read_csv('income-restricted-inventory-2020.csv')
data_2020['Year'] = 2020

data_2021 = pd.read_csv('income-restricted-inventory-2021.csv')
data_2021['Year'] = 2021

data_2022 = pd.read_csv('income-restricted-housing-inventory-2022.csv')
data_2022['Year'] = 2022

# Concatenating all dataframes
all_data = pd.concat([data_2020, data_2021, data_2022])

total_residences_per_year = all_data.groupby('Year')['Total Income-Restricted'].sum().reset_index()

# Ploting 
plt.figure(figsize=(10, 5))
print(total_residences_per_year)

plt.plot(total_residences_per_year['Year'], total_residences_per_year['Total Income-Restricted'], marker='o')
plt.title('Total Residences by Year')
plt.xlabel('Year')
plt.ylabel('Total Residences')
plt.grid(True)
plt.xticks(total_residences_per_year['Year'])  
plt.tight_layout()
plt.show()
