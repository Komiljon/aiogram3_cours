from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hello! {message.from_user.first_name}')


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Помощь!')


@router.message(F.text == 'Как дела?')
async def ask_t(message: Message):
    await message.answer('Я в порядке.')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer('Это картинка.')
