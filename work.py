from binance.client import Client
import config

client = Client(config.api_key, config.api_secret)
print("login")

# info = client.get_symbol_info("BTCUSDT")
# for x, y in info.items():
#     print(x, y)
info = client.get_account()
balans = info['balances']
for x in balans:
    # print(x)
    if float(x['free']) > 0:
        print(x)