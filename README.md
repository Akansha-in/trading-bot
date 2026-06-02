# Binance Futures Testnet Trading Bot

A Python CLI application to place futures orders on Binance USDT-M Testnet.
Built with clean separation between the API client, order logic, and CLI interface.

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py 
│   ├── client.py 
│   ├── orders.py
│   └── logger.py
├── logs/
│   └── bot.log 
├── cli.py 
├── requirements.txt 
└── README.md
```

---

## Features

- Place **MARKET** and **LIMIT** orders on Binance Futures Testnet
- Supports both **BUY** and **SELL** sides
- Input validation with clear error messages
- All API requests and responses logged to `logs/bot.log`
- Error handling for API errors, network failures, and invalid input

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/trading-bot.git
cd trading-bot
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Get Binance Testnet API credentials

1. Go to [testnet.binance.com](https://testnet.binance.com)
2. Log in with Google
3. Find the **API Key** section on the dashboard
4. Click **Generate** — copy both the API Key and Secret immediately
   (Secret is shown only once)

### 4. Set your API keys

**Windows PowerShell:**
```powershell
$env:BINANCE_TESTNET_API_KEY="your_api_key_here"
$env:BINANCE_TESTNET_API_SECRET="your_api_secret_here"
```

**Mac/Linux:**
```bash
export BINANCE_TESTNET_API_KEY="your_api_key_here"
export BINANCE_TESTNET_API_SECRET="your_api_secret_here"
```


---

## How to Run

### Place a MARKET order
```powershell
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT order
```powershell
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3200.00
```

### More examples
```powershell
#Selling BTC at market price
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

# Buying ETH with a limit order
python cli.py --symbol ETHUSDT --side BUY --type LIMIT --quantity 0.05 --price 3100.00
```

---

## Logs

Every order request and response is automatically saved to `logs/bot.log`.

Example log entry:
```
2026-06-01 14:02:11 | INFO | Placing order: BTCUSDT | BUY | MARKET | qty=0.001 | price=None
2026-06-01 14:02:12 | INFO | Response: {'orderId': 4751923810, 'status': 'FILLED', 'executedQty': '0.001', 'avgPrice': '67432.10000'}
```

---

## All CLI Arguments

| Argument   | Required          | Description                              |
|------------|-------------------|------------------------------------------|
| --symbol   | Yes               | Trading pair, must end in USDT. Example: BTCUSDT |
| --side     | Yes               | BUY or SELL                              |
| --type     | Yes               | MARKET or LIMIT                          |
| --quantity | Yes               | Amount to trade                          |
| --price    | Only for LIMIT    | Limit price                              |
