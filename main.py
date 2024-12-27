from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask, request
import os

# Create a Flask app
app = Flask(__name__)

# Define a start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your simple Telegram bot. How can I help you?')

# Define a function to handle text messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Main function to set up the bot
def main() -> None:
    # Replace with your bot's API token from BotFather
    token = 'YOUR_API_TOKEN'

    # Create an Updater object and pass in the API token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Register a message handler that will echo text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot in a separate thread
    updater.start_polling()

    # Run the Flask app (this is for Koyeb to bind to port 8080)
    app.run(host='0.0.0.0', port=8080)

# If running as the main module, run the bot
if __name__ == '__main__':
    main()
