import telegram
from telegram.ext import Updater, CommandHandler

import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

token = '5012538289:AAHh88BNDl33qQARZXnzKKpviVi1lvLYa0U'

# Bot functions come here
# /getid - Reply the chat id
def getId(bot, update, user_data):
    logging.debug("{}".format(user_data))
    print(user_data)
    print(update.message.from_user.id)
    update.message.reply_text(update.message.from_user.id)

def main():
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("getid", getId, pass_args=True))
    updater.start_polling()

if __name__ == '__main__':
    main()