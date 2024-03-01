import pandas as pd
import matplotlib.pyplot as plt


'''The Point of this data is to compare the top 5 zip codes with the most income-restricted housing over the years'''



data_2020 = pd.read_csv('income-restricted-inventory-2020.csv')
data_2020['Year'] = 2020

data_2021 = pd.read_csv('income-restricted-inventory-2021.csv')
data_2021['Year'] = 2021

data_2022 = pd.read_csv('income-restricted-housing-inventory-2022.csv')
data_2022['Year'] = 2022

all_data = pd.concat([data_2020, data_2021, data_2022])

# Identify the five most populous zip codes based on the total residences over all years
top_zip_codes = all_data.groupby('Zip Code')['Total Income-Restricted'].sum().nlargest(5).index

# Filter the data to include only the top five zip codes
filtered_data = all_data[all_data['Zip Code'].isin(top_zip_codes)]

grouped_data = filtered_data.groupby(['Zip Code', 'Year'])['Total Income-Restricted'].sum().reset_index()
pivot_table = grouped_data.pivot(index='Year', columns='Zip Code', values='Total Income-Restricted')

# Ploting
plt.figure(figsize=(10, 5))
for zip_code in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[zip_code], marker='o', label=str(zip_code))
plt.title('Total Residences by Year for Top 5 Zip Codes')
plt.xlabel('Year')
plt.ylabel('Total Residences')
plt.legend(title='Zip Code')
plt.grid(True)
plt.xticks(pivot_table.index)  
plt.tight_layout()
plt.show()
