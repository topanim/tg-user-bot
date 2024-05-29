import asyncio
from random import randint
from typing import Any, Callable

from colorama import Fore
from pyrogram import Client, filters
from pyrogram.filters import Filter
from pyrogram.handlers import MessageHandler
from pyrogram.handlers.handler import Handler
from pyrogram.methods.messages.get_chat_history import get_chunk
from pyrogram.types import Chat, Message, Photo

api_id = 20151498
api_hash = "1023d2a541f723a15c4796c564d66043"

daivinchik = "leomatchbot"


async def is_that_girl(client: Client, message: Message):
    name = " "
    if message.caption is None:
        return

    is_girl = (name.lower() in (message.caption or '').lower())

    caption = message.caption.split(", ")[0]

    if is_girl:
        print(Fore.GREEN + "Найдена: " + caption)
        await download_photos_of_message(client, message)
        client.remove_handler(get_handler())
    else:
        print(Fore.RED + "Несовпадение: " + caption)


handler = MessageHandler(
    callback=is_that_girl,
    filters=filters.chat(daivinchik) & ~filters.me
)


def get_handler(): return handler


async def main():
    async with Client("some_man", api_id, api_hash) as app:
        app: Client

        # some = await wait_for(app, daivinchik)
        # print(some)
        #
        # message: Message = await find_girl(app, "some_man")
        # print(message)

        app.add_handler(
            get_handler()
        )

        while True:
            send = "👎"
            await app.send_message(daivinchik, send)
            await asyncio.sleep(randint(2, 5))

        # if message.chat.id:
        #     file_id = message.photo.file_id
        #     file_size = message.photo.file_size
        #     file_path = await app.download_media(message)
        #     print(f"Загружена фотография {file_id} размером {file_size} в файл {file_path}")


async def download_photos_of_chat(client: Client, chat_id: int | str):
    photos = []
    async for photo in client.get_chat_photos(chat_id=chat_id):
        photos.append(photo)
    # print(me)

    for photo in photos:
        photo: Photo
        big_file_id = photo.file_id

        # Используйте полученные file_id для загрузки изображений
        big_photo = await client.download_media(big_file_id)

        print(big_photo)


async def download_photos_of_message(client: Client, message: Message):
    for photo in message.photo.thumbs:
        file_id = photo.file_id
        await client.download_media(file_id)


class Awaiting:
    message = None


async def wait_for(
        client: Client,
        chat_id: int | str
):
    awaiting = Awaiting()

    def callback(_: Client, message: Message):
        awaiting.message = message

    client.add_handler(

    )

    while True:
        if awaiting.message is not None:
            return awaiting.message
        await asyncio.sleep(1)


async def find_girl(client: Client, name: str):
    # chat: Chat = await client.get_chat(daivinchik)
    send = "👎"

    await client.send_message(daivinchik, send)

    while True:
        message = await wait_for(client, daivinchik)

        # print(vars(message))

        # if len(keyboard[0]) <= 2:
        #     send = keyboard[0][-2]
        # else:

        await asyncio.sleep(randint(2, 5))
        await client.send_message(daivinchik, send)


asyncio.run(main())
