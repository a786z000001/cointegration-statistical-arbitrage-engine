import yfinance as yf
import pandas as pd

def load_data(stock1, stock2, start_date):
    data1 = yf.download(stock1, start=start_date)['Close']
    data2 = yf.download(stock2, start=start_date)['Close']

    df = pd.concat([data1, data2], axis=1)
    df.columns = ['stock1', 'stock2']
    df = df.dropna()

    return df