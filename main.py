#!/usr/bin/python
from sys import argv
from script import *

if __name__ == "__main__":
    
    if argv[1] == "--help":
        print("Type ./main.py and the number of orders\n"
               "Like ./main.py 5, to see 5 orders")
    else:       
        info = get_data("ticker")
        orderbook = get_data("orderbook")
        process_orderbook(orderbook, argv[1])
        process_general_data(info)
