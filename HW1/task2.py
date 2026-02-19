# 2.1.1
from IPython.display import display

# df = df.drop('tsunamiEventId', 'earthquakeEventId', 'volcanoLocationId', 
#              'volcanoLocationNewNum', 'volcanoLocationNum', 'location', 'latitude',
#              'elevation', 'morphology', 'agent', 'deathsTotal', 'deathsAmountOrderTotal',
#              'significant', 'publish', 'eruption', 'status', 'timeErupt', 'deathsAmountOrder',
#              'damageAmountOrder', 'housesDestroyedAmountOrderTotal', 'deaths', 'injuries')

tmp = ['date', 'country', 'name', 'vei']

new_df = df.groupby('country')

for country_name, grouped_df in new_df:
    country_df = grouped_df[tmp]
    country_df = country_df.sort_values('vei', ascending=False)
    
    display(country_df)

# 2.1.2
maximum_vei = df.groupby('country')['vei']

for country_name, country_vei in maximum_vei:
    print(f"Country: {country_name}, Highest VEI: {country_vei}")

#2.1.3
import matplotlib.pyplot as plt
import numpy as np

eruption_freq = df['name'].value_counts()
volcanoes = eruption_freq[eruption_freq > 4].index

for v in volcanoes:
    
    new_df = df[df['name'] == v].sort_values('date')
    x = new_df['date']
    y = new_df['vei']

    plt.figure(figsize=(5, 2.7), layout='constrained')
    plt.plot(x, y, label='linear')
    plt.xlabel('date')
    plt.ylabel('VEI')
    plt.title(f"VEI Over Time: {v}")
    plt.legend()
    plt.show()
