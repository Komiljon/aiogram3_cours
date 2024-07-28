import asyncio
import logging

from config import TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Помощь!')


@dp.message(F.text == 'Как дела?')
async def ask_t(message: Message):
    await message.answer('Я в порядке.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
