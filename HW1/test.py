import pandas as pd
d = ['21/06/2025', '22/06/2025']
res = pd.to_datetime(d, format='%d/%m/%Y')
print(res)