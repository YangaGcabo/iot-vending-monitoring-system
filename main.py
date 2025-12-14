import random
import time

STOCK_THRESHOLD = 10
stock_level = 50

def read_sensor():
    return random.randint(1, 5)

while True:
    sold = read_sensor()
    stock_level -= sold

    print(f"Items sold: {sold}, Stock left: {stock_level}")

    if stock_level <= STOCK_THRESHOLD:
        print("⚠️ ALERT: Restock required!")

    time.sleep(2)
