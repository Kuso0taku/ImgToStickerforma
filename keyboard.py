from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


btn_help = KeyboardButton('/help')
btn_clear = KeyboardButton('/clear')
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_help.add(btn_help)
kb_help.add(btn_clear)
