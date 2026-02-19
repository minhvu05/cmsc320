# 3.1.1
query = '''
SELECT AVG(TotalPay)
FROM Salaries
WHERE LOWER(JobTitle) LIKE '%clerk%'
    AND Year BETWEEN 2011 AND 2014
'''

# KEEP THIS. It will display the whole dataframe.
df = pd.read_sql(query, conn)
df

# 3.1.2
query = '''
SELECT * 
FROM Salaries
WHERE LOWER(JobTitle) LIKE '%clerk%'
    AND Year = 2013
    AND TotalPay < 50000
ORDER BY TotalPay DESC
'''
# KEEP THIS. It will display the whole dataframe.
df = pd.read_sql(query, conn)
df

# 3.1.3
query = '''
SELECT
    AVG(BasePay) AS avg_base_pay,
    AVG(Benefits) AS avg_benefits,
    AVG(OvertimePay) AS avg_overtime_pay,
    AVG(BasePay) + AVG(Benefits) + AVG(OvertimePay) AS total_avg_compensation    
FROM Salaries
WHERE Lower(JobTitle) LIKE '%clerk%'
    AND JobTitle NOT GLOB '%SENIOR%'

'''

# KEEP THIS. It will display the whole dataframe.
df = pd.read_sql(query, conn)
df

# 3.1.4
# idk if need
# import sqlite3
# import pandas as pd 

# conn = sqlite3.connect("database.sqlite")
# crsr = conn.cursor()

years = [2010, 2011, 2012, 2013, 2014, 2015]

for year in years:
    query = f'''
    SELECT *
    FROM Salaries
    WHERE Year = {year}
    '''

    new_df = pd.read_sql_query(query, conn)
    table_name = f"Salary_{year}"
    df.to_sql(table_name, conn, if_exists='append')    


