import urllib.request
from json import loads

def get_data(type):
    try:
        request = urllib.request.urlopen("https://api.blinktrade.com/api/v1/BRL/" + type)

    except:
        raise RunTimeError("Request failed")
    
    data = loads(request.read().decode("utf-8")) # parses json
    return data    

def process_orderbook(data, amount):
    bids = data["bids"]
    asks = data["asks"]
    print("Buy orders")
    for i in range(0, amount):
        bids[i].pop(-1)
        print(bids[i])

    print("\n" + "Sell orders")
    for i in range(0, amount):
        asks[i].pop(-1)
        print(asks[i])

def process_general_data(data):
    print("\nLast buy: " + str(data["last"]))


info = get_data("ticker")
orderbook = get_data("orderbook")
process_orderbook(orderbook, 3)
process_general_data(info)

