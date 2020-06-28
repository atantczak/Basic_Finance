# This is the FOURTH 'Python Programming for Finance' episode from sentdex. 

# This is a program graphing stock data, of your choosing, using the popular candlestick graphing method. 
# I'm covering two different methods here so please note the divide separating the two. 

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import pandas as pd
import pandas_datareader.data as web
import mpl_finance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')
# This is simply a style choice. Feel free to look into others once you get going. 

df = pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)
# You can read from many different file formats such as: json, SQL, excel, etc.)

# You can resample the data to different increments. For instance, stock data is produced daily and you will
# receive the data in daily increments. If you're analyzing the lifetime of a certain stock, all of this data is
# unecessary to save. Therefore, you can follow the following process in order to resample the data and make it come
# in 10 day increments (or whatever other increment you might want).

df_ohlc = df['Adj Close'].resample('10D').ohlc()
# Open, high, low, close = "ohlc"

df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1) , (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()

###################################################################### METHOD 2 ######################################################################
import plotly.graph_objects as go

ticker = 'TSLA'
df = pd.read_csv('{}.csv'.format(ticker),parse_dates=True, index_col=0)

df.index = pd.to_datetime(df.index)

fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Adj Close'],
                                     increasing_line_color='darkcyan',
                                     decreasing_line_color='darkgray')])
fig.update_layout(title="{} Stock".format(str(ticker)),
                  xaxis_title="Date",
                  yaxis_title="{} Stock Price".format(str(ticker)))

fig.show()
