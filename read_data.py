# This is the SECOND 'Python Programming for Finance' episode from sentdex. 

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
# This is simply a style choice. Feel free to look into others once you get going. 


'''
Important to note: You need to write the file path as seen below. Let's say I have a folder titled "Stocks"; that's why
I tell the "filename" portion of the command to go to "Stocks/AAPL.csv" ... if I was already in the folder with the AAPL
data, I would simply write 'AAPL.csv'. Often times, however, you will keep data in separate folders. 
'''
df = pd.read_csv('Stocks/AAPL.csv',parse_dates=True, index_col=0)
# Parse_dates ensures the format of all dates will be legible.
# index_col = 0 is telling it to treat the first column as the index, or 0th column.
# You can read from many different file formats such as: json, SQL, excel, etc.)

df['Adj Close'].plot()
plt.show()

'''
I chose to only plot adjusted close here. Of course, you can plot the highs, volume, or whatever else you may want to
look at. This is where the awesome powers of customization come into play. When you get comfortable with this stuff, you
can really make all of these your own.
'''
