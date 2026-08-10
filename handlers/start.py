from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_menu
from utils.database import add_or_update_user

router = Router()


WELCOME_TEXT = """
<b>👋 Welcome to Session Generator Bot!</b>

🔐 Generate Telegram sessions through
a simple and secure interface.

⚡ Fast
🛡️ Privacy-focused
📱 Pyrogram & Telethon support

Choose an option below.
"""


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    user = message.from_user

    if user is not None:
        add_or_update_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
        )

    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_menu(),
    )
