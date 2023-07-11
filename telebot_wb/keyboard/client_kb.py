# прописка кнопок

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/смартфоны')
b2 = KeyboardButton('/компьютеры')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)# меняет клавиатуру на модульную

kb_client.add(b1).add(b2)