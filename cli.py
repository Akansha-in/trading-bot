import argparse
import os
from bot.orders import run_order

def interactive_mode(api_key, api_secret):
    print("\n=============================")
    print("  Binance Futures Trading Bot")
    print("=============================\n")

    # Symbol
    symbol = input("Enter symbol (e.g. BTCUSDT): ").strip().upper()
    if not symbol:
        print("❌ Symbol cannot be empty")
        return

    # Side
    print("\nSelect side:")
    print("  1. BUY")
    print("  2. SELL")
    side_choice = input("Enter 1 or 2: ").strip()
    if side_choice == "1":
        side="BUY"
    elif side_choice == "2":
        side="SELL"
    else:
        print("❌ Invalid choice. Enter 1 or 2")
        return

    # Order type
    print("\nSelect order type:")
    print("  1. MARKET")
    print("  2. LIMIT")
    print("  3. STOP")
    type_choice = input("Enter 1, 2, or 3: ").strip()
    if type_choice == "1":
        order_type = "MARKET"
    elif type_choice == "2":
        order_type = "LIMIT"
    elif type_choice == "3":
        order_type = "STOP"
    else:
        print("❌ Invalid choice. Enter 1, 2, or 3")
        return

    # Quantity
    try:
        quantity = float(input("\nEnter quantity: ").strip())
    except ValueError:
        print("❌ Quantity must be a number")
        return

    price = None
    if order_type in ["LIMIT", "STOP"]:
        try:
            price = float(input("Enter price: ").strip())
        except ValueError:
            print("❌ Price must be a number")
            return

    print()
    run_order(api_key, api_secret, symbol, side, order_type, quantity, price)

def main():
    api_key=os.environ.get("BINANCE_TESTNET_API_KEY")
    api_secret=os.environ.get("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        print("❌ API keys not found.")
        print("Run these first:")
        print('  $env:BINANCE_TESTNET_API_KEY="your_key"')
        print('  $env:BINANCE_TESTNET_API_SECRET="your_secret"')
        return

    import sys
    if len(sys.argv) == 1:
        interactive_mode(api_key, api_secret)
        return

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET, LIMIT, or STOP_MARKET")
    parser.add_argument("--quantity", required=True, type=float, help="How much to buy/sell")
    parser.add_argument("--price", required=False, type=float, help="Price for LIMIT or STOP_MARKET orders")

    args = parser.parse_args()

    run_order(
        api_key= api_key,
        api_secret= api_secret,
        symbol= args.symbol,
        side= args.side,
        order_type= args.type,
        quantity= args.quantity,
        price= args.price
    )

if __name__ == "__main__":
    main()