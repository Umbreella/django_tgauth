from os import getenv
from typing import Optional

import aiohttp
from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, User

router = Router(name='cmd_start_router')


@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject) -> None:
    token: Optional[str] = command.args

    if token is None:
        return

    async with aiohttp.ClientSession(
        base_url=getenv('DJANGO_BACK')
    ) as session:
        user: Optional[User] = message.from_user

        if user is None:
            return

        payload: dict = {
            'token': token,
            'user_data': {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'external_id': user.id,
            },
        }

        async with session.post(
            url='/api/private/v1.0/tgRegistration',
            json=payload,
        ):
            pass
