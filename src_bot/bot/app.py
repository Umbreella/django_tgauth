from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src_bot.bot.routers.add_routers import add_routers

load_dotenv()


async def run() -> None:
    bot: Bot = Bot(token=getenv('BOT_TOKEN', ''))
    dp: Dispatcher = Dispatcher()

    add_routers(dispatcher=dp)

    await dp.start_polling(bot)
