import urllib.request
from json import loads

def get_info():
    try:
        request = urllib.request.urlopen("https://api.blinktrade.com/api/v1/BRL/orderbook")

    except:
        raise RunTimeError("Request failed")
    
    info = loads(request.read().decode("utf-8")) # parses json
    return info

print(get_info())
