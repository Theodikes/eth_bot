from urllib.error import HTTPError
from urllib.request import urlopen as get
from threading import Timer
import json

BINANCE_API_GET_ETH_PRICE_LINK = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
BOT_TOKEN = "YOUR_TOKEN"
TELEGRAM_CHANNEL_NAME = "@your_channel_link"
TELEGRAM_API_SEND_MESSAGE_LINK = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL_NAME}&text="
CHECK_PRICE_INTERVAL_IN_SECONDS = 5


def send_price_to_channel(price: int):
    full_request_link = f'{TELEGRAM_API_SEND_MESSAGE_LINK}{price}$'
    try:
        get(full_request_link)
    except HTTPError:
        pass


def get_eth_price_from_binance() -> int:
    try:
        data = json.load(get(BINANCE_API_GET_ETH_PRICE_LINK))
        rounded_price = int(float(data["price"]))
        return rounded_price
    except HTTPError:
        return -1


def main():
    Timer(CHECK_PRICE_INTERVAL_IN_SECONDS, main).start()
    current_eth_price = get_eth_price_from_binance()
    if current_eth_price == -1:
        return
    send_price_to_channel(current_eth_price)


Timer(CHECK_PRICE_INTERVAL_IN_SECONDS, main).start()
