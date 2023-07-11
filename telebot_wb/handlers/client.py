from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboard.client_kb import kb_client
from handlers import parser_WB



# ________________________Клиентская часть_____________________________
# общение с ботом
# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('общение с ботом через ЛС, напишите ему\nhttps://t.me/cakes33_bot')

# @dp.message_handler(commands=['Режим_работы'])
async def cakes_open(message : types.Message):
    lst = parser_WB.main()
    for i in range(0, len(lst), 20):
        group = lst[i:i+20]
        await bot.send_message(message.from_user.id, str(group))

# @dp.message_handler(commands=['Место_работы'])
async def cakes_map(message : types.Message):
    await bot.send_message(message.from_user.id, '222222')


    
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(cakes_open, commands=['смартфоны'])
    dp.register_message_handler(cakes_map, commands=['компьютеры'])
