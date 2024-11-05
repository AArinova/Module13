from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from babel.plural import skip_token

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands=["start"])
async def mess_start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_massages(message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)