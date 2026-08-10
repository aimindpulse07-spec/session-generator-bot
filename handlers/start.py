from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    name = (
        message.from_user.first_name
        if message.from_user
        else "User"
    )

    text = (
        f"👋 <b>Welcome, {name}!</b>\n\n"
        "🔐 <b>Session Generator Bot</b>\n\n"
        "Your secure Telegram utility bot.\n\n"
        "Use /help to see available commands."
    )

    await message.answer(text)
