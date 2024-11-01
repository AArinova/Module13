from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from babel.plural import skip_token

api = "7245377370:AAHM2WCQKtOFuRQzZyuV2MakYowLQgObyyA"
bot = Bot(token = api)
db = Dispatcher(bot, storage = MemoryStorage())

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)