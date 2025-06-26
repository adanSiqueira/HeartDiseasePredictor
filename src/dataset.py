from data.data_loader import ProcessedData
data = ProcessedData()
df = data.get_data()

df_ill = df.query('ill == 1')
df_not_ill = df.query('ill == 0')