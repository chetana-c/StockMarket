import pandas as pd


#database to excel
Df = pd.read_csv('time_series_covid19_confirmed_global.csv')
print(Df)
Df.to_csv(r'/Users/cchetana/MyDocs/stock_details.csv', sep='\t', index=False, header=True)
new_df = pd.read_csv(r'/Users/cchetana/MyDocs/stock_details.csv')
print(new_df)


