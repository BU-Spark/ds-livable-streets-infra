
import pandas as pd

data_2022 = pd.read_csv('income-restricted-housing-inventory-2022.csv')

# Calculate the average number of residences per zip code for 2022
average_residences_per_zip_2022 = data_2022.groupby('Zip Code')['Total Income-Restricted'].mean().reset_index()

# Renaming
average_residences_per_zip_2022.columns = ['Zip Code', 'Average Residences 2022']

print(average_residences_per_zip_2022)
