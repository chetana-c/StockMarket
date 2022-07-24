import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#define the ticker symbol
tickerSymbol = ['RELIANCE.BO']
#MSFT', '^DJI', 'NFTY','RELIANCE.BO'
#get data on this ticker
count = 0

for tkr in tickerSymbol:
    if tkr != '':
        count = count + 1
        tickerData = yf.Ticker(tkr)
        tickerDf = tickerData.history(period='1d', start='2020-7-5', end='2020-8-24')
        print(tickerDf)
        tickerDf.to_csv(r'/Users/cchetana/MyDocs/stock_details.csv', sep='\t', index=False, header=True)
        new_df = pd.read_csv(r'/Users/cchetana/MyDocs/stock_details.csv')
        print(new_df)
        avg_price = (tickerDf.High+tickerDf.Low)/2
        tickerDf['Average'] = avg_price
        #tickerDf.plot(y='High')
        #tickerDf.plot(y='Open')
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 7), sharex=False)
        ax2 = tickerDf.plot(y='High',ax=axes[0], color='orange', kind='line')
        ax4 = tickerDf.plot(y='Open',ax=axes[1], kind='line')
        plt.title('Stock analysis of ' + tkr)
        plt.tight_layout()
        plt.plot()
#plt.show()
print(tickerDf.shape)

        #fig.savefig('my_plot.png')