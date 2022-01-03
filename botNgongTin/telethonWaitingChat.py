from telethon import TelegramClient, events, sync
import os
import time
from botSender import *

"""
Chờ tin nhắn từ 1 channel
Chỉ cần nick chính có trong channel đó là có thể lấy tin
Khi lấy tin về nếu có image thì sẽ download về và gủi tin đó bằng bot dựa trên chat id
=============
Nick Chạy Thật
Name: Duy Manh
api_id: 12851949
api_hash: 85488a8a42f94b9e7e30ef025c9fa6bd
=============
Nick Test
Name: Kim Ngan
api_id: 12648870
api_hash: 85595b9b263644e903466852866c3f2c
"""
api_id = 12648870
api_hash = '85595b9b263644e903466852866c3f2c'
image_path = 'image'
client = TelegramClient('my', api_id, api_hash)
phone_number = '+84563719489'
channel = 1482304924 #Channel Anh Kha: Free Signals - Tín hiệu miễn phí
# channel = 1603147951 #Channel Test: Channel DuyManhDev Draw

# @client.on(events.ChatAction)
# async def handler(event):
#     # Welcome every new user
#     print(event.user_joined)
#     print(event.added_by)
#     print(event.action_message.id )
#     if event.user_joined:
#         await event.reply('Welcome to the group!')

@client.on(events.NewMessage(chats=channel))
async def my_event_handler(event):
    """
    Gởi tin trực tiếp bằng nick chính. làm vậy dể bị die nick
    if event.raw_text: await client.send_message(entity=entity, message=event.raw_text)
    if event.media: await client.send_file(entity=entity, file=event.media, caption=event.raw_text)
    """
    path = ''
    print(event.raw_text)
    if event.raw_text and event.media:
        path = await event.download_media(image_path + '/photo')
        sendFileHasCaption(file=path, caption=event.raw_text)
    elif event.raw_text:
        sendMessage(message=event.raw_text)
    elif event.media:
        path = await event.download_media(image_path + '/photo')
        sendFile(file=path)
    # sendNote(message='Vào Group CSKH: https://t.me/+7GdlqbeHeDU1ZDFl Tham Giá Các Cuộc Hội Thoại Cùng Các Nhà Phân Tích.')
    # sendNote(message='Vào Kênh: https://t.me/sarafxcom Để Nhận Được Nhiều Tín Hiệu Hơn.')
    if path:
        time.sleep(2)
        await emptyFileInFolders(image_path)

async def emptyFileInFolders(path):
    root = path
    folders = list(os.walk(root))[1:]
    for folder in folders:
        if not folder[2]:
            await os.rmdir(folder[0])

client.start()
client.run_until_disconnected()