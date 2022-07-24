from yahoo_fin import stock_info as si
from pprint import pprint
from pandas import json_normalize
from time import time, sleep
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 18)

dfs = pd.DataFrame()
x = 0
while x <= 10:
    sleep(60 - time() % 60)
    symbols = ["RCOM.NS", "RNAVAL.NS", "RPOWER.NS", "IDEA.NS"]
    for sym in symbols:
        live_price = si.get_live_price(sym)
        data = si.get_quote_table(sym)
        #dfs.append(data)
        df = json_normalize(data)
        df['Live Price'] = live_price
        df['Symbol'] = sym
        newdf = df[['Symbol','Live Price','Previous Close', 'Open', 'Quote Price', '52 Week Range']]
        #print(newdf)
        final_df = pd.concat([dfs,newdf], axis=0)
        dfs = final_df
    x = x + 1
print(dfs)

dfs.to_csv(r'/Users/cchetana/MyDocs/stock_live_price.csv', sep='\t', index=False, header=True)
new_df = pd.read_csv(r'/Users/cchetana/MyDocs/stock_live_price.csv')
print(new_df)
