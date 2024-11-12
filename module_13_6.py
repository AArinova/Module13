from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from babel.plural import skip_token
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = "7245377370:AAHM2WCQKtOFuRQzZyuV2MakYowLQgObyyA"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# """keyboard"""
# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button = KeyboardButton(text="Рассчитать")
# button_info = KeyboardButton(text="Информация")
# kb.row(button, button_info)-

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data = 'formulas')
kb.add(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(call):
    pass

@dp.callback_query_handler(text="formulas")


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()
    
"""кнопка Старт"""
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет!", reply_markup = kb)

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await UserState.weight.set()
    data = await state.get_data()
    norma = 10*int(data["weight"])+6.25*int(data["growth"])-5*int(data["age"])-161
    await message.answer(f"Ваша норма калорий: {norma} Ккал в день .")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)