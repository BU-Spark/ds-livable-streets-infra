import pandas as pd
import matplotlib.pyplot as plt


'''This was the code used to create the bar plot for the number of residences per zip code in 2022'''

def plot_residences_per_zipcode(csv_file_path):
    data = pd.read_csv(csv_file_path)

    residences_per_zip = data.groupby('Zip Code')['Total Income-Restricted'].sum()

    # Sorting
    sorted_residences_per_zip = residences_per_zip.sort_values(ascending=False)

    # Plotting
    plt.figure(figsize=[10, 6])
    sorted_residences_per_zip.plot(kind='bar', color='skyblue')
    plt.title('Number of Residences by Zip Code')
    plt.xlabel('Zip Code')
    plt.ylabel('Total Project Units')
    plt.xticks(rotation=45)  # Rotating the x-axis labels for better readability
    plt.grid(axis='y')
    plt.show()

csv_file_path = 'income-restricted-housing-inventory-2022.csv'  
plot_residences_per_zipcode(csv_file_path)
