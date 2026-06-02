from bot.client import place_order

def validate_inputs(symbol, side, order_type, quantity, price):
    # Checking symbol
    if not symbol.endswith("USDT"):
        print("❌ Symbol must end with USDT. Example: BTCUSDT")
        return False
    
    # Checking side
    if side not in ["BUY", "SELL"]:
        print("❌ Side must be BUY or SELL")
        return False
    
    # Checking order type
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        print("❌ Order type must be MARKET, LIMIT, or STOP")
        return False
    
    # Checking quantity
    if quantity <= 0:
        print("❌ Quantity must be greater than 0")
        return False
    
    # Price is required for LIMIT orders
    if order_type in ["LIMIT", "STOP"] and (price is None or price <= 0):
        print(f"❌ Price is required for {order_type} orders and must be greater than 0")
        return False
    
    return True

def run_order(api_key, api_secret, symbol, side, order_type, quantity, price=None):
    symbol=symbol.upper()
    side=side.upper()
    order_type=order_type.upper()
    
    # Validate input
    is_valid = validate_inputs(symbol, side, order_type, quantity, price)
    if not is_valid:
        return
    
    # Printing order summary
    print("\n--- ORDER SUMMARY ---")
    print(f"Symbol    : {symbol}")
    print(f"Side      : {side}")
    print(f"Type      : {order_type}")
    print(f"Quantity  : {quantity}")
    if price:
        print(f"Price     : {price}")
    print("---------------------\n")
    
    # Placing the order
    result = place_order(api_key, api_secret, symbol, side, order_type, quantity, price)
    
    if result is None:
        print("❌ Order failed. Check logs/bot.log for details.")
        return
    
    if "code" in result and result["code"] < 0:
        print(f"❌ Order failed: {result['msg']}")
        return
    
    print("--- ORDER RESULT ---")
    print(f"Order ID    : {result.get('orderId')}")
    print(f"Status      : {result.get('status')}")
    print(f"Executed Qty: {result.get('executedQty')}")
    print(f"Avg Price   : {result.get('avgPrice', 'N/A')}")
    print("--------------------")
    print("✅ Order placed successfully!\n")