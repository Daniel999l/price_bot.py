import time
import requests
from telebot import TeleBot

TELEGRAM_BOT_TOKEN = "7643579258:AAERkZvLPE5r4WvmLHWqmKcGrcOyB2N0CV8"
COINMARKETCAP_API_KEY = "0cd48446-3939-49db-9b6f-835927a81b04"
CRYPTOCURRENCY_SYMBOL = "TNSR"
CHECK_INTERVAL_SECONDS = 300

bot = TeleBot(TELEGRAM_BOT_TOKEN)
USER_ID = 6473954258  # Replace this with your Telegram user ID

def fetch_price():
    try:
        headers = {
            "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY
        }
        params = {
            "symbol": CRYPTOCURRENCY_SYMBOL
        }
        response = requests.get(
            "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
            headers=headers,
            params=params
        )
        data = response.json()
        price = data["data"][CRYPTOCURRENCY_SYMBOL]["quote"]["USD"]["price"]
        return round(price, 5)
    except Exception as e:
        print(f"Error: {e}")
        return None

while True:
    price = fetch_price()
    if price:
        bot.send_message(USER_ID, f"The price of {CRYPTOCURRENCY_SYMBOL} is ${price}")
    else:
        bot.send_message(USER_ID, "Failed to fetch price.")
    time.sleep(CHECK_INTERVAL_SECONDS)
