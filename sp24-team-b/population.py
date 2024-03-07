import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('displacement.csv')
areas_of_interest = ['Boston']
filtered = df[df['municipal'].isin(areas_of_interest)]


race_columns = ['totpop','nhwhi','nhaa','nhas']
population_data = filtered[['municipal','acs_year'] + race_columns]

print(population_data)

grouped_data = population_data.groupby('acs_year').sum()

plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
for race in race_columns:
    plt.plot(grouped_data.index, grouped_data[race], label=race)

plt.title('Population of Different Races Over the Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()