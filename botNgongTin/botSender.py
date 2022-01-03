from telegram import Bot

channelInputChatID = -1001440713082 #Channel Name: Sarafx Forex Signals
groupChatID = -1001680342558 #Group name: Chia Sẽ Tỷ Giá Phát Sinh CFDs
token = '5073025070:AAH4mS0ZEPolCvTsG3HvwghIKxDPyYKAECU' #TinHieuForex_Bot
# channelInputChatID = -1001716714383 #Channel Name: Dev_Channel_Show_news test input
# groupChatID = -1001561707211 #Group name: Group_Test_Bot
# token = '5012538289:AAHh88BNDl33qQARZXnzKKpviVi1lvLYa0U' #Bot Dev_Tin_Hieu_bot
bot = Bot(token)

def delete_message(chat_id, message_id)-> None:
    if chat_id and message_id:
        bot.delete_message(chat_id=chat_id, message_id=message_id)

def sendMessage(message)-> None:
    if message:
        bot.send_message(channelInputChatID, message)
        bot.send_message(groupChatID, message)
    return True

def sendFileHasCaption(file, caption)-> None:
    if file and caption:
        bot.send_photo(channelInputChatID, photo=open(file, 'rb'), caption=caption)
        bot.send_photo(groupChatID, photo=open(file, 'rb'), caption=caption)

def sendNote(message)-> None:
    if message:
        bot.send_message(groupChatID, message)

def sendFile(file)-> None:
    if file:
        bot.send_photo(channelInputChatID, photo=open(file, 'rb'))