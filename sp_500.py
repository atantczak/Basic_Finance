# This is the FIFTH and SIXTH 'Python Programming for Finance' episode from sentdex.

# The purpose of this is to pull all the data from the S&P 500 and save it within a directory of your choosing.
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


'''
This first segment is known as a function with returns something specific, in this case, a list of tickers. 
You then will "call" this function as seen in line 39. This function goes onto Wikipedia to get the list of stocks
within the SP500. I'm using totally different methods nowadays but will sometimes still use this function because, if
I'm searching for a good buying opportunity based on some criteria, I might want to search through a large group of 
stocks to find that buying opportunity. There are few better options than the SP500!
'''

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        mapping=str.maketrans(".","-")
        ticker=ticker.translate(mapping)
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


save_sp500_tickers()


'''
This function is using what we started with and applying it a little differently. Notice how we're saving dataframes
to files just as we did in a previous code. Now, however, we're having it run through all SP500 tickers and do that. 
This is known as a for loop. Essentially it's saying "For each ticker that you see within my list of tickers, grab the
data from yahoo and save that data within a file titled "{}.csv".format(ticker) ... this part is cool because it allows
you to change the name of the file based on the ticker that is currently being saved. IE ~ if the ticker is 'AAPL', this 
line is telling the code to save the file as 'AAPL.csv'. That {} is left blank and the .format(ticker) portion is telling
it what to put within the curly brackets ... I digress. If you'd like to learn more about the specifics of coding, check out 
all the awesome tutorials online!
'''


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000, 1, 1)
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

# The last few lines were edited based on: https://stackoverflow.com/questions/58708111/keyerror-historicalpricestore

get_data_from_yahoo(True)