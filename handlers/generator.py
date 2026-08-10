from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.generator import auth_method_menu, library_menu
from utils.session_state import session_states

router = Router()


GENERATOR_TEXT = """
🔐 <b>Choose Library</b>

Select which library you want to use:

📱 <b>Pyrogram</b>
Generate a Pyrogram-compatible session.

📡 <b>Telethon</b>
Generate a Telethon-compatible session.
"""


AUTH_TEXT = """
🔐 <b>Choose Authentication Method</b>

Select how you want to authenticate:

🔢 <b>OTP</b>
Authenticate using Telegram's login code.

📷 <b>QR Code</b>
Authenticate using a Telegram QR code.

⚠️ Never share your OTP, 2FA password,
or generated session with anyone.
"""


@router.callback_query(F.data == "generate")
async def generate_callback(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        GENERATOR_TEXT,
        reply_markup=library_menu(),
    )
    await callback.answer()


@router.callback_query(
    F.data.in_({"library_pyrogram", "library_telethon"})
)
async def library_callback(callback: CallbackQuery) -> None:
    library = (
        "pyrogram"
        if callback.data == "library_pyrogram"
        else "telethon"
    )

    if callback.from_user is None:
        await callback.answer("Unable to identify user.", show_alert=True)
        return

    await session_states.create(
        user_id=callback.from_user.id,
        library=library,
    )

    await callback.message.edit_text(
        AUTH_TEXT,
        reply_markup=auth_method_menu(library),
    )

    await callback.answer()


@router.callback_query(F.data.startswith("auth_"))
async def auth_method_callback(callback: CallbackQuery) -> None:
    if callback.from_user is None:
        await callback.answer("Unable to identify user.", show_alert=True)
        return

    data = callback.data or ""

    if ":" not in data:
        await callback.answer("Invalid authentication method.", show_alert=True)
        return

    method, library = data.split(":", 1)

    if method not in {"auth_otp", "auth_qr"}:
        await callback.answer("Invalid authentication method.", show_alert=True)
        return

    state = await session_states.get(callback.from_user.id)

    if state is None or state.library != library:
        await callback.answer(
            "Your session has expired. Please start again.",
            show_alert=True,
        )
        return

    state.method = "otp" if method == "auth_otp" else "qr"

    await callback.answer(
        f"{state.method.upper()} selected."
    )

    # Actual authentication will be implemented separately.
    await callback.message.edit_text(
        f"""
✅ <b>{library.title()}</b> selected.

🔐 Authentication method:
<b>{state.method.upper()}</b>

The secure authentication flow will be connected
in the next step.
""",
    )


@router.callback_query(F.data == "close")
async def close_callback(callback: CallbackQuery) -> None:
    if callback.from_user is not None:
        await session_states.delete(callback.from_user.id)

    await callback.message.delete()
    await callback.answer()
