from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

def get_stocks_data(stock):
    data = pdr.get_data_yahoo(stock, start = '2022-06-01', end=datetime.now(), interval="1h")  
    data = data.reset_index()
    return data 

