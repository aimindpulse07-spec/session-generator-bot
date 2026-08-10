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


def auth_method_menu(library: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔢 OTP",
                    callback_data=f"auth_otp:{library}",
                ),
                InlineKeyboardButton(
                    text="📷 QR Code",
                    callback_data=f"auth_qr:{library}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Back",
                    callback_data="generate_back",
                ),
                InlineKeyboardButton(
                    text="✖️ Close",
                    callback_data="close",
                ),
            ],
        ]
    )
