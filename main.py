import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.bot import Bot
from getNews import *

token = '5073025070:AAH4mS0ZEPolCvTsG3HvwghIKxDPyYKAECU'
channelInputChatID = -1001440713082

def upToChannel(update: Update, context: CallbackContext) -> None:
    chatId = channelInputChatID
    bot = Bot(token)
    dataNews = get_news_Tradingview()
    bot.send_message(chatId, f'Chia sẽ tín hiệu {dataNews[0]["code"].strip()}: \n {dataNews[0]["title"].strip()} \n {dataNews[0]["description"].strip()}')
    bot.send_photo(chatId, dataNews[0]["link"])
    update.message.reply_text('Đã cập nhật tin tức lên Channel')

def reviewTinTradingview(update: Update, context: CallbackContext) -> None:
    dataNews = get_news_Tradingview()
    update.message.reply_text(f'Chia sẽ tín hiệu {dataNews[0]["code"].strip()}: \n {dataNews[0]["title"].strip()} \n {dataNews[0]["description"].strip()}')
    update.message.reply_photo(dataNews[0]["link"])

def status(update, context: CallbackContext) -> None:
    statusStr = f'<a href="https://sarafx.com/">{update.effective_user.last_name} {update.effective_user.first_name}<a/>' + ' Command Bot SaraFX\n▫/reviewTinTradingview xem trước tin tức\n▫/upToChannel up tin tức đó vào channel\n'
    update.message.reply_text(statusStr)

def main():
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('reviewTinTradingview', reviewTinTradingview))
    updater.dispatcher.add_handler(CommandHandler('upToChannel', upToChannel))
    updater.dispatcher.add_handler(CommandHandler('status', status))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()