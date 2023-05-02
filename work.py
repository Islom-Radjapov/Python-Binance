from binance.client import Client
import config
from datetime import datetime, timedelta

client = Client(config.api_key, config.api_secret)
print("login")
#
# # info = client.get_symbol_info("BTCUSDT")
# # for x, y in info.items():
# #     print(x, y)
# info = client.get_account()
# balans = info['balances']
# for x in balans:
#     # print(x)
#     if float(x['free']) > 0:
#         print(x)


def get_candle_1h_before(time):
    start = str(time - timedelta(hours=5))
    end = str(time)
    df = pd.DataFrame(client.get_historical_klines(symbol="BNBUSDT", interval='1h', start_str=start, end_str=end))
    df = df.iloc[:, :5]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df