# This is the THIRD 'Python Programming for Finance' episode from sentdex. 

# The purpose is alter local data to view certain aspects of it.

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
# This is simply a style choice. Feel free to look into others once you get going. 
'''
Important to note: You need to write the file path as seen below. This is a file path on my computer, but will not
be the same on yours unless you go out of your way to make it the same. For instance, if you're searching for the 
NFLX.csv file, you would simply need to know where it is located. Maybe it's in a folder titled "Stocks", in which case
your path would be "Stocks/NFLX.csv'. 
'''
df = pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)
# You can read from many different file formats such as: json, SQL, excel, etc.)

df['100ma'] = df['Adj Close'].rolling(window=100).mean()
# 100ma means the 100 day moving average. 
# A moving average is the average of the stock price for today and the 99 days preceding. 
# df.dropna(inplace=True)
# This redefines df in order to move the calculation to the first value where calculating
# the 100 day moving average is possible. 


# df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
# This will also work. It won't calculate the moving average if it is not possible. 
# It will just give you the price.

'''
Below helps you set up subplots for your graph. Perhaps you want to graph the stock price with the volume below. 
If you're going to do that manually, you'll need subplots. You're sizing and positioning the subplots in the below two
lines. While I could provide a walkthrough of how to do this, matplotlib will do a lot better job! Go online and
search for their awesome tutorials. 
'''

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

'''
The below three lines are setting up the graph based on what you want it to display. This will display the closing prices,
the 100 day moving average, and the volume on a separate plot. At the end, you always need to write plt.show() or else
the code won't know you want to view it!
'''

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()

