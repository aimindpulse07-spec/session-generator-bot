from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("me"))
async def me_handler(message: Message) -> None:
    user = message.from_user

    if user is None:
        await message.answer(
            "❌ Unable to retrieve your Telegram information."
        )
        return

    username = (
        f"@{user.username}"
        if user.username
        else "Not set"
    )

    language = user.language_code or "Unknown"

    text = (
        "👤 <b>Your Telegram Information</b>\n\n"
        f"🆔 <b>User ID:</b> <code>{user.id}</code>\n"
        f"👤 <b>Name:</b> {user.full_name}\n"
        f"🔗 <b>Username:</b> {username}\n"
        f"🌐 <b>Language:</b> {language}\n"
        f"🤖 <b>Bot:</b> {'Yes' if user.is_bot else 'No'}"
    )

    await message.answer(text)
