from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from utils.database import add_or_update_user


class UserTrackingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[
            [TelegramObject, Dict[str, Any]],
            Awaitable[Any],
        ],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User | None = data.get("event_from_user")

        if user is not None:
            add_or_update_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
            )

        return await handler(event, data)
