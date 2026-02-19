# importing required libraries
import pandas as pd
import requests

# 1.0
api_url = "https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/volcanoes"

req = requests.request('GET', api_url)
tmp = req.json().get("items")
print(tmp)

df = pd.DataFrame(tmp)
df.to_csv("volcanoes.csv")



# 1.1.1
df.describe()

# 1.1.2
df.info()

# 1.1.3
new_df = df[["id", "year", "month", "tsunamiEventId", "earthquakeEventId", "volcanoLocationId", 
             "volcanoLocationNewNum", "name", "country", "elevation", "morphology", "deathsTotal", 
             "vei", "deaths"]]



# 1.2.1
df.dropna(subset=["year", "month", "day"])

# 1.2.2
# df.set_index('id') ??
df.rename(index=lambda x: x + 1)

# 1.2.3
# df['totalDeaths'] = df[['totalDeaths', 'deaths']].max(axis=1)
df.assign(totalDeaths = df[['deathsTotal','deaths']].max(axis=1))



# 1.3
import datetime
import pandas as pd

# df[['year','month','day']]
# df['date'] = pd.to_datetime(df[['year','month','day']])

# is this right, do i have to drop NaN?

# Drop original columns and sort.
df = df[df['year'] > 1677] 
df = df[df['month'] > 0] 
df = df[df['day'] > 0] 
df['date'] = pd.to_datetime(df[['year','month','day']]) 
df = df.sort_values(['date']) 

df = df.drop(['year', 'month', 'day'], axis=1)

# Place new column next to 'id' column.
tmp = df.pop('date')
df.insert(1, 'date', tmp)

new_df
# # KEEP THIS. It will display the whole dataframe.
new_df




