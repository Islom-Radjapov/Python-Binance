# candel plots
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'])
                     ])
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

def klines(symbol):
    df = pd.DataFrame(client.get_historical_klines(symbol, '1h', '26h UTC'))
    # df = pd.DataFrame(client.get_historical_klines(symbol, '1m', '40m UTC'))
    df = df.iloc[:,:6]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df



ta.trend.macd(df.close).iloc[-1], ta.trend.macd_signal(df.close).iloc[-1], bnb_macd.iloc[-1]