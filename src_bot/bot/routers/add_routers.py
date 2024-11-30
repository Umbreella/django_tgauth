from aiogram import Dispatcher

from src_bot.bot.routers.commands import start


def add_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(start.router)
