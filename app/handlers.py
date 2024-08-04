from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keybords as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hello! {message.from_user.first_name}', reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Помощь!', reply_markup=kb.settings)


@router.message(F.text == 'Cars?')
async def ask_t(message: Message):
    await message.answer('Cars.', reply_markup=await kb.inline_cars())


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer('Это картинка.')


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('fdsfdsfs', show_alert=True)
    await callback.message.edit_text('Catalog chous', reply_markup=await kb.inline_cars())
