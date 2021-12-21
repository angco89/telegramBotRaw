from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.bot import Bot

token = '5012538289:AAHh88BNDl33qQARZXnzKKpviVi1lvLYa0U'
channelInputChatID = -1001716714383

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def sendMessage(message)-> None:
    chatId = channelInputChatID
    bot = Bot(token)
    if message:
        bot.send_message(chatId, message)

def sendFile(file)-> None:
    chatId = channelInputChatID
    bot = Bot(token)
    if file:
        bot.send_photo(chatId, file)

def main():
    """Start the bot."""
    updater = Updater("5012538289:AAHh88BNDl33qQARZXnzKKpviVi1lvLYa0U")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()