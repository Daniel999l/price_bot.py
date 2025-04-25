import time
import requests
from telebot import TeleBot
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Your Telegram Bot Token and CoinMarketCap API Key
TELEGRAM_BOT_TOKEN = "7643579258:AAERkZvLPE5r4WvmLHWqmKcGrcOyB2N0CV8"
COINMARKETCAP_API_KEY = "0cd48446-3939-49db-9b6f-835927a81b04"
CRYPTOCURRENCY_SYMBOL = "TNSR"
CHECK_INTERVAL_SECONDS = 300  # How often to check the price (in seconds)

# Initialize the bot
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

@app.route('/')
def index():
    # Only run the price fetch function once for testing
    price = fetch_price()
    if price:
        bot.send_message(USER_ID, f"The price of {CRYPTOCURRENCY_SYMBOL} is ${price}")
        return f"Price of {CRYPTOCURRENCY_SYMBOL}: ${price}"
    else:
        return "Failed to fetch price."

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
