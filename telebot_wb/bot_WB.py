
#  ФАЙЛ ТОЧКА ВХОДА
from aiogram.utils import executor
from create_bot import dp
from handlers import parser_WB



# вывод в консоль что бот онлайн
async def on_start(_):
    print("bot online")

from handlers import client,  other, parser_WB

parser_WB
client.register_handlers_client(dp)
# admin.register_handler_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)


