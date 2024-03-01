import pandas as pd

'''Overall Statistics mentioned in the report ''' 

'''This is a compilation of a number of statistics that are important to the report. I used these several times through out 
The report.'''





'''TOTAL NUMBER OF RESIDENCES'''

data_2020 = pd.read_csv('income-restricted-inventory-2020.csv')
data_2020['Year'] = 2020
data_2022 = pd.read_csv('income-restricted-housing-inventory-2022.csv')

total_residences_2022 = data_2022['Total Income-Restricted'].sum()

# Print out the total number of residences for 2022
print(f'Total number of residences for 2022: {total_residences_2022}')


'''Averages per zipcode in 2022'''

total_residences = data_2022['Total Income-Restricted'].sum()

# Num of unique zip codes
unique_zip_codes = data_2022['Zip Code'].nunique()

# Overall average 
overall_average_residences = total_residences / unique_zip_codes

median_residences = data_2022['Total Income-Restricted'].median()
std_dev_residences = data_2022['Total Income-Restricted'].std()

print(f'Overall Average Number of Residences per Zip Code in 2022: {overall_average_residences}')
print(f'Overall Median Number of Residences in 2022: {median_residences}')
print(f'Overall Standard Deviation of Residences in 2022: {std_dev_residences}')


'''Averages per zipcode in 2022'''

# Calculate the average number of residences per zip code for 2022
average_residences_per_zip_2022 = data_2022.groupby('Zip Code')['Total Income-Restricted'].mean().reset_index()

average_residences_per_zip_2022.columns = ['Zip Code', 'Average Residences 2022']

print(average_residences_per_zip_2022)


'''RATE OF INCREASE'''


# sum the total residences for 2020
total_residences_2020 = data_2020['Total Income-Restricted'].sum()

# sum the total residences for 2022
total_residences_2022 = data_2022['Total Income-Restricted'].sum()

# Calculate the rate of increase from 2020 to 2022
rate_of_increase = ((total_residences_2022 - total_residences_2020) / total_residences_2020) * 100

print(f'Rate of Increase from 2020 to 2022: {rate_of_increase:.2f}%')
