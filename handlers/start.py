from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_menu

router = Router()


WELCOME_TEXT = """
👋 <b>Welcome!</b>

🤖 <b>Session Generator Bot</b>

Use the buttons below to explore the bot.

⚠️ Never share your Telegram OTP,
2FA password, or authentication credentials.
"""


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_menu(),
    )
