import logging

from aiogram import Router
from aiogram.types import ErrorEvent

from utils.logger import logger


router = Router()


@router.error()
async def global_error_handler(
    event: ErrorEvent,
) -> bool:
    logger.exception(
        "Unhandled bot error: %s",
        event.exception,
    )

    try:
        if event.update.message:
            await event.update.message.answer(
                "⚠️ Something went wrong.\n"
                "Please try again in a moment."
            )
        elif event.update.callback_query:
            await event.update.callback_query.answer(
                "⚠️ Something went wrong. Please try again.",
                show_alert=True,
            )
    except Exception:
        logging.getLogger(__name__).exception(
            "Failed to send error message to user."
        )

    return True
