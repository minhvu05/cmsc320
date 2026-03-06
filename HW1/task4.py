# 4.1
# Create the Sample dataset from above flowchart
input_data = {
    'account': ['383080', '383080', '383080', '412290', '412290','412290','412290','412290','218895','218895','218895','218895'],
    'order': ['10001', '10001', '10001', '10005', '10005','10005','10005','10005','10006','10006','10006','10006'],
    'ext_price': [235.83, 232.32, 107.97, 2679.36, 286.02, 832.95, 3472.04, 915.12, 3061.12, 518.65, 216.9, -72.18]
}

# Create DataFrame
df = pd.DataFrame(input_data)

# Display Dataframe (DONT REMOVE THE CODE)
display(df)

# 4.2
# Group by 'order' and show intermediate result
grouped = df.groupby('order')

# Display intermediate result for each group; hints: you have to use 'for loop'
for g in grouped:
    display(g)

# 4.3
# Repeat group by 'order' again and then apply aggregation (sum of 'ext_price' for each 'order')
summed = df.groupby('order')
summed = summed['ext_price'].sum()

# Show the aggregated result after re-grouping  (DONT REMOVE THE CODE)
display(summed)

# 4.4
# Reset index to combine result into a single DataFrame
final = summed.reset_index()

# Rename the columns for clarity
final = final.rename(columns = {'ext_price':'Order_Total'})


# Show the final result  (DONT REMOVE THE CODE)
display(final)
