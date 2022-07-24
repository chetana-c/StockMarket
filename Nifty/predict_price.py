from nsetools import Nse
from pprint import pprint
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection
import matplotlib.pyplot as plt
import rpy2.robjects as robjects
from datetime import datetime
import six
import smtplib
from rpy2.robjects.packages import importr

import numpy as np

def main():
    desired_width = 320
    par = robjects.r('par')
    # forecast=importr('forecast')

    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 20)

    nse = Nse()
    x = nse.get_top_gainers()
    # pprint(x)
    top_gainers_df = pd.DataFrame(x)
    # print(top_gainers_df.head())
    pprint(top_gainers_df.symbol)
    tickerSymbol_raw = top_gainers_df['symbol'].to_list()
    append_str = ".NS"
    tickerSymbol = [sub + append_str for sub in tickerSymbol_raw]
   # tickerSymbol = ["IDEA.NS"]
    pprint(tickerSymbol)
    count = 0
    rows = []
    for tkr in tickerSymbol:
        if tkr != '':
            count = count + 1
            tickerData = yf.Ticker(tkr)
            start = datetime(2020, 8, 1)
            end = datetime.now()
            tickerDf = tickerData.history(period='1d', start=start, end=end)
            print("History Data of ",tkr, "is: \n",tickerDf)
            tickerDf['prediction'] = tickerDf['Close'].shift(-1)
            tickerDf.dropna(inplace=True)
            days = 10
            forecast_time = int(days)
            X = np.array(tickerDf.drop(['prediction'], 1))
            Y = np.array(tickerDf['prediction'])
            X = preprocessing.scale(X)
            X_prediction = X[-forecast_time:]
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.5)
            # Performing the Regression on the training data
            clf = LinearRegression()
            clf.fit(X_train, Y_train)
            prediction = (clf.predict(X_prediction))
            # print(tickerDf)
            # print(prediction)
            last_row = tickerDf.tail(1)
            if (float(prediction[4]) > (float(last_row['Close']))):
                output = ("\nStock " + str(tkr) + "\nPriorCLose:\n" + str(
                    last_row['Close']) + "\n\nPredicition 1 Day: " + str(
                    prediction[0]) + "\n\n: Prediction in 7 Days:" + str(prediction[6]))
                # print(output)
                rows.append([str(tkr), str(tickerDf['Close'].iloc[-1]), str(prediction[0]), str(prediction[6])])
               # print("**************************************************")
            if (float(prediction[4]) < (float(last_row['Close']))):
                output = ("\nStock " + str(tkr) + "\nPriorCLose:\n" + str(
                    last_row['Close']) + "\n\nPredicition 1 Day: " + str(
                    prediction[0]) + "\n\n: Prediction in 7 Days:" + str(prediction[6]))
                rows.append([str(tkr), str(tickerDf['Close'].iloc[-1]), str(prediction[0]), str(prediction[6])])
                #sendMessage(output)
                # print(output)
    print(rows)
    df = pd.DataFrame(rows, columns=["Top 10 gainers", "Close Value", "Prediction in 1 Day", "Prediction in 7 Days"])
    print(df)
    fig = render_mpl_table(df, header_columns=0, col_width=2.0)
    print(fig)
    plt.show()

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax


def sendMessage(text):
    # If you're using Gmail to send the message, you might need to
    # go into the security settings of your email account and
    # enable the "Allow less secure apps" option
    username = "EMAIL"
    password = "PASSWORD"

    vtext = "PHONENUMBER@vtext.com"
    message = text

    msg = """From: %s
    To: %s
    %s""" % (username, vtext, message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, vtext, msg)
    server.quit()

    print('Sent')


if __name__ == '__main__':
    main()

