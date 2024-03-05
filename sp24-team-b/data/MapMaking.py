import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

boston = gpd.read_file('Boston_Neighborhoods.geojson')

northEnd = 'North End'
downtown = 'Downtown'

boston['color'] = '#cccccc' 
boston.loc[boston['Name'] == northEnd, 'color'] = 'red'
boston.loc[boston['Name'] == downtown, 'color'] = 'blue'

# Create legend patches
red_patch = mpatches.Patch(color='red', label=northEnd)
blue_patch = mpatches.Patch(color='blue', label=downtown)

fig, ax = plt.subplots(1, 1)
boston.plot(color=boston['color'], ax=ax)

plt.legend(handles=[red_patch, blue_patch])

plt.title('Map of Boston')

plt.show()
