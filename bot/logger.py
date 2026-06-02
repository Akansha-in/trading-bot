import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("trading_bot")
logger.setLevel(logging.DEBUG)

#Removing old handlers
if logger.handlers:
    logger.handlers.clear()

#File handler
file_handler = logging.FileHandler("logs/bot.log", mode="a")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

#Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))

logger.addHandler(file_handler)
logger.addHandler(console_handler)