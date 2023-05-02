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


class MACDStrategy:
    def __init__(self, fast_period=12, slow_period=26, signal_period=9):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def generate_signals(self, df):
        # Calculate MACD and Signal line values
        macd_indicator = ta.trend.MACD(df['Close'], self.fast_period, self.slow_period, self.signal_period)
        macd = macd_indicator.macd()
        signal = macd_indicator.macd_signal()

        # Generate buy and sell signals based on MACD crossover with Signal line
        buy_signals = (macd > signal) & (macd.shift(1) < signal.shift(1))
        sell_signals = (macd < signal) & (macd.shift(1) > signal.shift(1))

        # Combine signals into a single DataFrame
        signals = pd.DataFrame(index=df.index)
        signals['positions'] = 0
        signals.loc[buy_signals, 'positions'] = 1
        signals.loc[sell_signals, 'positions'] = -1

        return signals

