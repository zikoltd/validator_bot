import os
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.environ.get('TELEGRAM_VALIDATOR_TOKEN')

def validate_address(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text('Please provide an address. Example: /validate 0x...')
        return
    
    address = ' '.join(context.args)
    is_btc = validate_btc(address)
    is_eth = validate_eth(address)
    
    if is_btc:
        update.message.reply_text('✅ Valid Bitcoin address')
    elif is_eth:
        update.message.reply_text('✅ Valid Ethereum address')
    else:
        update.message.reply_text('❌ Invalid cryptocurrency address')

def validate_btc(address):
    # Basic BTC address validation
    return re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address)

def validate_eth(address):
    # Basic ETH address validation
    return re.match(r'^0x[a-fA-F0-9]{40}$', address)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Welcome to Wallet Validator Bot!\n'
        'Send /validate [address] to check validity\n'
        'Supports BTC and ETH addresses'
    )

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("validate", validate_address))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()