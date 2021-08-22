import os
from client import FtxClient

client = FtxClient(api_key=os.environ['api_key'], api_secret=os.environ['api_secret'])

enable = ['USD', 'USDT']

for coin in client.lending_info():
    if coin['coin'] in enable:
        print(coin)
        client.submit_lending_offer(coin=coin['coin'], size=coin['lendable'], rate=coin['minRate'])