from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_URL


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📚 Help",
                    callback_data="help",
                ),
                InlineKeyboardButton(
                    text="💬 Support",
                    url=SUPPORT_URL,
                ),
            ]
        ]
    )
