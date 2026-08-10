import time

import psutil
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.database import get_user_count

router = Router()

START_TIME = time.monotonic()


def format_uptime(seconds: float) -> str:
    seconds = int(seconds)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    parts = []

    if days:
        parts.append(f"{days}d")

    if hours:
        parts.append(f"{hours}h")

    if minutes:
        parts.append(f"{minutes}m")

    parts.append(f"{seconds}s")

    return " ".join(parts)


@router.message(Command("stats"))
async def stats_handler(message: Message) -> None:
    user_count = get_user_count()

    cpu = psutil.cpu_percent(interval=0.2)
    memory = psutil.virtual_memory()

    uptime = format_uptime(
        time.monotonic() - START_TIME
    )

    text = (
        "📊 <b>Bot Statistics</b>\n\n"
        f"👥 <b>Users:</b> {user_count}\n"
        f"🖥️ <b>CPU:</b> {cpu:.1f}%\n"
        f"🧠 <b>RAM:</b> {memory.percent:.1f}%\n"
        f"⏱️ <b>Uptime:</b> {uptime}\n"
    )

    await message.answer(text)
