from nsetools import Nse
from pprint import pprint
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

import numpy as np

desired_width=320
par=robjects.r('par')
#forecast=importr('forecast')

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)

nse = Nse()
x = nse.get_top_gainers()
rcom = nse.get_
#pprint(x)
top_gainers_df = pd.DataFrame(x)
print(top_gainers_df.head())
pprint(top_gainers_df.symbol)
tickerSymbol_raw = top_gainers_df['symbol'].to_list()
append_str = ".NS"
tickerSymbol = [sub + append_str for sub in tickerSymbol_raw]
pprint(tickerSymbol)
count = 0
for tkr in tickerSymbol:
    if tkr != '':
        count = count + 1
        tickerData = yf.Ticker(tkr)
        tickerDf = tickerData.history(period='1d', start='2020-7-5', end='2020-8-22')
        # print(tickerDf)
        avg_price = (tickerDf.High+tickerDf.Low)/2
        tickerDf['Average'] = avg_price
        #tickerDf.plot(y='High')
        #tickerDf.plot(y='Open')
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 7), sharex=False)
        ax2 = tickerDf.plot(y='High',ax=axes[0], color='orange', kind='line')
        ax4 = tickerDf.plot(y='Close',ax=axes[1], kind='line')
        plt.title('Stock analysis of ' + tkr)
        plt.tight_layout()
        plt.plot()
#plt.show()


#data = pd.read_html("https://finance.yahoo.com/most-active")
#print(data)