import asyncio
import logging

from src_bot.bot.app import run

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run())
