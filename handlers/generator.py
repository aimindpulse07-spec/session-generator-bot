from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.generator import library_menu

router = Router()


GENERATOR_TEXT = """
🔐 <b>Choose Library</b>

Select which library you want to use:

📱 <b>Pyrogram</b>
Generate a Pyrogram-compatible session.

📡 <b>Telethon</b>
Generate a Telethon-compatible session.
"""


@router.callback_query(F.data == "generate")
async def generate_callback(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        GENERATOR_TEXT,
        reply_markup=library_menu(),
    )
    await callback.answer()


@router.callback_query(F.data == "close")
async def close_callback(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.answer()
