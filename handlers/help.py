from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


HELP_TEXT = """
📚 <b>Help & Commands</b>

Here are the available commands:

🟢 <b>/start</b>
Open the main menu.

🔐 <b>/gen</b>
Open the session generator.

📱 <b>/genp</b>
Generate a Pyrogram session.

📡 <b>/gent</b>
Generate a Telethon session.

👤 <b>/me</b>
View your Telegram information.

📊 <b>/stats</b>
View bot statistics.

❓ <b>/help</b>
Show this help message.

⚠️ <i>Never share your OTP, 2FA password,
or generated session with anyone.</i>
"""


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(HELP_TEXT)


@router.callback_query(F.data == "help")
async def help_callback(callback: CallbackQuery) -> None:
    await callback.message.edit_text(HELP_TEXT)
    await callback.answer()
