from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def library_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📱 Pyrogram",
                    callback_data="library_pyrogram",
                ),
                InlineKeyboardButton(
                    text="📡 Telethon",
                    callback_data="library_telethon",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✖️ Close",
                    callback_data="close",
                ),
            ],
        ]
    )
