
# Calculate overall average, median, and standard deviation
import pandas as pd

data_2022 = pd.read_csv('income-restricted-housing-inventory-2022.csv')



total_residences = data_2022['Total Income-Restricted'].sum()

# Number of unique zip codes
unique_zip_codes = data_2022['Zip Code'].nunique()

# Overall average 
overall_average_residences = total_residences / unique_zip_codes

median_residences = data_2022['Total Income-Restricted'].median()
std_dev_residences = data_2022['Total Income-Restricted'].std()


print(f'Overall Average Number of Residences per Zip Code in 2022: {overall_average_residences}')
print(f'Overall Median Number of Residences in 2022: {median_residences}')
print(f'Overall Standard Deviation of Residences in 2022: {std_dev_residences}')
