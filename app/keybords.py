from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Catalog')],
#     [KeyboardButton(text='Basket'), KeyboardButton(text='Contacts')]
# ],
#     resize_keyboard=True,
#     input_field_placeholder='Выбрать из меню')

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Catalog', callback_data='catalog')],
    [InlineKeyboardButton(text='Basket', callback_data='basket'),
     InlineKeyboardButton(text='Contacts', callback_data='contacts')]
],
    resize_keyboard=True,
    input_field_placeholder='Выбрать из меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Aptechestvo', url='https://aptechestvo.ru')]
])

cars = ['Mers', 'BMW', 'Audi', 'Tesla']


async def inline_cars():
    keybard = InlineKeyboardBuilder()
    for car in cars:
        keybard.add(InlineKeyboardButton(text=car, url='https://aptechestvo.ru'))
    return keybard.adjust(2).as_markup()
