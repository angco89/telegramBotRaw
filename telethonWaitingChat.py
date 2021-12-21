from telegram import chat
from telethon import TelegramClient, events, sync
from botTelethon import *

# Remember to use your own values from my.telegram.org!
api_id = 12851949
api_hash = '85488a8a42f94b9e7e30ef025c9fa6bd'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='Dev_Channel_Test_Bot'))
async def my_event_handler(event):
    print(event.photo)
    print(event.file)
    print(event.media)
    print(event.raw_text)
    print(event)
    # await client.send_message(entity='Dev_Channel_Show_news', message=event.raw_text)
    # await client.send_message(entity='Dev_Channel_Show_news', file=event.media)
    await client.send_file(entity='Dev_Channel_Show_news', file=event.media, caption=event.raw_text)
    # await client.send_media(entity='Dev_Channel_Show_news', message=event.media)
    # if event.raw_text:
    #     sendMessage(message=event.raw_text)
    # if event.file:
    #     sendFile(file=event.file)
    # client.send_message(entity='Dev_Channel_Show_news', message=event.raw_text)

client.start()
client.run_until_disconnected()