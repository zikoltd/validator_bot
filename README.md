# Wallet Validator Bot

A Telegram bot that validates Bitcoin and Ethereum wallet addresses.

## Features

- Validates Bitcoin (BTC) addresses
- Validates Ethereum (ETH) addresses
- Simple command interface
- Real-time validation responses

## Usage

1. Start the bot with `/start`
2. Validate an address using `/validate [address]`

Example:
```
/validate 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
```

## Setup

1. Set your Telegram bot token as an environment variable:
```bash
export TELEGRAM_VALIDATOR_TOKEN='your_token_here'
```

2. Install required dependencies:
```bash
pip install python-telegram-bot
```

3. Run the bot:
```bash
python validator_bot.py
```

## Validation Rules

- BTC: Addresses start with 1 or 3, length 26-35 characters
- ETH: Addresses start with 0x, followed by 40 hexadecimal characters

## Requirements

- Python 3.6+
- python-telegram-bot
- Operating system with environment variable support
