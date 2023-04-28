# candel plots
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'])
                     ])
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

