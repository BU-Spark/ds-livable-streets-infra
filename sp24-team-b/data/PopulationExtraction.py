import matplotlib.pyplot as plt

# Data
years = [2010, 2015, 2017, 2020]
population = {
    'White': [7888, 8287, 8158, 9306],
    'Black/African American': [53, 1, 556, 141],
    'Hispanic': [308, 364, 278, 528],
    'Asian/PI': [250, 273, 92, 445],
    'Other': [109, 182, 185, 385]
}

fig, ax = plt.subplots()

ax.stackplot(years, population.values(), labels=population.keys())

ax.set_title('Population in North End (2010 - 2020)')
ax.set_xlabel('Year')
ax.set_ylabel('Population')

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()

plt.show()