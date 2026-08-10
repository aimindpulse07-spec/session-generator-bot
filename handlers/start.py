from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_menu

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
    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_menu(),
    )
