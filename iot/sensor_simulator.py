import random
import time

def read_stock_level():
    return random.randint(0, 100)

if __name__ == "__main__":
    while True:
        print("Stock level:", read_stock_level())
        time.sleep(5)
