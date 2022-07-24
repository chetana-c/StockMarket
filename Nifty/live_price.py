from yahoo_fin import stock_info as si
from pprint import pprint
from pandas import json_normalize
from time import time, sleep
import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 18)
'''
def live_price_stock():
    symbols = ["RCOM.NS","RNAVAL.NS","RPOWER.NS","IDEA.NS"]

    for sym in symbols:
        live_price = si.get_live_price(sym)
        data = si.get_quote_table(sym)
        df = json_normalize(data)
        print("Quote Values of : ",sym)
        df['Live Price'] = live_price
        #pprint(df)
        newdf = df[['Live Price','Previous Close','Open','Quote Price','52 Week Range']]
        print(newdf)
'''

dfs = []
while True:
    sleep(60 - time() % 60)
    symbols = ["RCOM.NS", "RNAVAL.NS", "RPOWER.NS", "IDEA.NS"]
    for sym in symbols:
        live_price = si.get_live_price(sym)
        data = si.get_quote_table(sym)
        df = json_normalize(data)
        dfs.append(df)
        print("Quote Values of : ", sym)
        df['Live Price'] = live_price
        df['Symbol'] = sym
        newdf = df[['Live Price', 'Previous Close', 'Open', 'Quote Price', '52 Week Range']]
        #dfs.append()

print(dfs)
'''
def get_live_stock_data():
    while True:
        sleep(60 - time() % 60)
        symbols = ["RCOM.NS", "RNAVAL.NS", "RPOWER.NS", "IDEA.NS"]
        dfs = []
        for sym in symbols:
            df = get_live_price(sym)
            dfs.append(df)
        return dfs

def append_dataframes():
    final_df = []
    dfs = get_live_stock_data()
    final_df.append(dfs)
    print(final_df)
    final_df.to_csv(r'/Users/cchetana/MyDocs/live_price.csv', sep='\t', index=False, header=True)
    new_df = pd.read_csv(r'/Users/cchetana/MyDocs/live_price.csv')
    print(new_df)

def get_live_price(sym):
    #live_price = si.get_live_price(sym)
    data = si.get_quote_table(sym)
    df = json_normalize(data)
    df['Live Price'] = 100
    df['Symbol'] = sym
    newdf = df[['Live Price', 'Previous Close', 'Open', 'Quote Price', '52 Week Range']]
    return newdf

if __name__ == '__main__':
    append_dataframes()
'''