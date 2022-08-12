
import pandas as pd
from datetime import datetime





def ema(cierre,m_ema):
    ema=cierre.ewm(span=m_ema, adjust=False).mean()
    return ema

def tema(cierre,m_ema):
    ema1=ema(cierre,m_ema)
    ema2=ema(ema1,m_ema)
    ema3=ema(ema2,m_ema)
    tema=(3*ema1)-(3*ema2)+ema3
    return tema

def rsi(df):
    pd.options.mode.chained_assignment = None  # default='warn'
    price=df['Close']
    df['Price Diff'] = price.diff(1)
    data = df[['Close','Price Diff']]
    data['gain'] = data['Price Diff'].clip(lower=0).round(2)
    data['loss'] = data['Price Diff'].clip(upper=0).abs().round(2)
    # Get initial Averages
    window_length=14
    data['avg_gain'] = data['gain'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]
    data['avg_loss'] = data['loss'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]
    # Get WMS averages
    # Average Gains
    for i, row in enumerate(data['avg_gain'].iloc[window_length+1:]):
        data['avg_gain'].iloc[i + window_length + 1] =\
            (data['avg_gain'].iloc[i + window_length] *
            (window_length - 1) +
            data['gain'].iloc[i + window_length + 1])\
            / window_length
    # Average Losses
    for i, row in enumerate(data['avg_loss'].iloc[window_length+1:]):
        data['avg_loss'].iloc[i + window_length + 1] =\
            (data['avg_loss'].iloc[i + window_length] *
            (window_length - 1) +
            data['loss'].iloc[i + window_length + 1])\
            / window_length
    rs = data['avg_gain'] / data['avg_loss']
    rsi = 100 - (100 / (1.0 + rs))
    return rsi




