# This is the EIGHTH 'Python Programming for Finance' episode from sentdex.

'''
This code takes the compiled dataframe of all SP500 prices and assesses if they have any correlation. Generally speaking,
you'd likely change the reason you were using this code. It's potential and power for analysis, however, is amazing.

A fake example:
Let's say that you have found evidence that groups of stocks that Coke and Pepsi trade exactly possite one another ...
ie ~ when Coke goes up, Pepsi goes down. You could evaluate that claim using a correlation matrix like this. If their
correlation value is -1 (meaning total negative correlation), then yes, when one goes up, the other will go down.
'''
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import os
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import pickle
import numpy as np
import requests
import yfinance as yf

style.use('ggplot')

yf.pdr_override


def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['AAPL'].plot()
    #plt.show()
    df_corr = df.corr()
    print(df_corr.head())

    # We now want to visualize correlations.
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()


visualize_data()
