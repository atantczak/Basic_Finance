# This is the SEVENTH 'Python Programming for Finance' episode from sentdex.

# You'll notice that this code builds off of sp_500.py!!
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import pickle
import requests
import yfinance as yf

yf.pdr_override


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2020, 1, 1)
    # end = dt.datetime(2020,1,3)
    end = dt.datetime.now()

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            try:
                #df = web.DataReader(ticker, 'yahoo', start, end)
                df = web.DataReader(ticker.replace('.', '-'), 'yahoo', start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            except Exception as ex:
                print('Error:', ex)
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()

# The last few lines were edited based on: https://stackoverflow.com/questions/58708111/keyerror-historicalpricestore

# Our goal is to now compile Adj Close for all stocks into one data frame.
'''
There are many reasons you might want to do this. Most obviously, comparisons. Let's say you wanted to know which 
stocks out of the SP500 have the highest momentum through the first three days of the week because you think that Thursday
will be a great buying day. You could use this to generate a dataframe that shows the change in price for the last 5 days
for each stock within the SP500. You save that to a csv or an excel and you can rank the stocks based on that criteria. 

If you have questions about this type of thing, let me know! I'd love to help!
'''

def compile_data():
    with open("sp500tickers.pickle","rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    # sp500tickers.pickle allows you to access the most recently updated data ... as opposed to pulling from a CSV in
    # the directory that is no longer in the S&P 500.

    for count,ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        # Below is renaming the close price with the corresponding ticker so that we can have that be our first row.
        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        # Below is dropping the unwanted columns.
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            # Above: "If we were to divide count by 10, is the remainder 0?"
            # This gaurantees that it will print every 10 instead of every one.

            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')


compile_data()


