import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID_RAW = os.getenv("OWNER_ID", "0").strip()
SUPPORT_URL = os.getenv(
    "SUPPORT_URL",
    "https://t.me/your_support",
).strip()


def get_owner_id() -> int:
    try:
        return int(OWNER_ID_RAW)
    except ValueError:
        return 0


OWNER_ID = get_owner_id()


def validate_config() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. "
            "Please add BOT_TOKEN to your .env file."
        )

    if OWNER_ID <= 0:
        raise RuntimeError(
            "OWNER_ID is missing or invalid. "
            "Please add your Telegram numeric user ID."
        )
