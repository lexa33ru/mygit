# СОЗДАНИЕ БОТА
from aiogram import Bot, Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
# bot = Bot(token='6365376536:AAHanY43R8QgPpFF51G_3S1OCTt4dZCiZWs')
dp = Dispatcher(bot, storage=storage)

