# This is the first 'Python Programming for Finance' episode from sentdex on YouTube ... he's awesome! Check him out.

# The purpose is simply to pull financial data from the web.

'''
These group of lines that say import before them are at the beginning of every code, for any beginners. They're job
is to import the relevant "libraries". Libraries help us carry out certain commands, functions, etc.
'''

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



'''
These next two lines are defining where you want your data to start and end. For this example, it will attempt
to go all the way back to  Jan 1. of 2000 and pull TSLA data. Obviously, TSLA wasn't around then. In such a case, it
will pull the first data it can. Our endpoint is "now"; datetime is an awesome library that allows for that type of thing.
Your code will simply publish the last available day of trading. 
'''
start = dt.datetime(2000,1,1)
end = dt.datetime.now()

'''
This next line is using a library from Pandas (awesome source) to grab data from the web. The second entry ('yahoo') is
telling it which source to go through. Yahoo is a great, simple source that a ton of people use to get started. 
'''
df = web.DataReader('TSLA', 'yahoo', start, end)

# df is short for dataframe

# print(df.head(10))
# print(df.tail(10))

df.to_csv('TSLA.csv')

'''
The last three lines from above (two of them commented out) do different things. The df.head will give you the top 10
lines from the dataframe. The df.tail does the same for the last lines of the dataframe. 

Lastly, the df.to_csv will send the data to a csv file, which you can title within the command. One thing to note there, 
pandas is awesome and you can therefore, very simply, choose to type df.to_excel or some other file type, if you wish.

I recommend Googling (or posting to this blog) ANY questions you have! The internet will answer you. I will answer you. 
It seems to me, in my experience in this field, I was never far away from an answer. 
'''
