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
- Interactive menu mode when running `python cli.py` with no arguments

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

1. Go to [testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Log in with Google
3. Find the **API Key** section on the dashboard
4. Click **Generate** and copy both the API Key and Secret immediately

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

### Interactive menu (no arguments needed)
```powershell
python cli.py
```
Launches a step-by-step menu to place orders without typing arguments.

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