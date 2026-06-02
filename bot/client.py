import hashlib
import hmac
import time
import requests
from urllib.parse import urlencode
from bot.logger import logger

BASE_URL = "https://testnet.binancefuture.com"

def get_server_time():
    try:
        response = requests.get(BASE_URL + "/fapi/v1/time", timeout=5)
        return response.json()["serverTime"]
    except:
        return int(time.time() * 1000)

def sign(params, secret):
    params["timestamp"] = get_server_time()
    query = urlencode(params)
    signature = hmac.new(
        secret.encode("utf-8"),
        query.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    params["signature"] = signature
    return params
def place_order(api_key, api_secret, symbol, side, order_type, quantity, price=None):
    url = BASE_URL + "/fapi/v1/order"

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    if order_type == "STOP_MARKET":
        params["stopPrice"] = price
    if order_type == "STOP":
        params["price"] = price
        params["stopPrice"] = price
        params["timeInForce"] = "GTC"

    params = sign(params, api_secret)
    headers = {
        "X-MBX-APIKEY": api_key
    }
    logger.info(f"Placing order: {symbol} | {side} | {order_type} | qty={quantity} | price={price}")
    # Sending the request
    try:
        response = requests.post(url, params=params, headers=headers, timeout=10)
        result = response.json()
        logger.info(f"Response: {result}")
        return result
    
    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        return None
    
    except requests.exceptions.ConnectionError:
        logger.error("Could not connect to Binance testnet")
        return None
    
    except Exception as e:
        logger.error(f"Something went wrong: {e}")
        return None