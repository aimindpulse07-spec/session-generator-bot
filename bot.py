import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, validate_config
from handlers.account import router as account_router
from handlers.generator import router as generator_router
from handlers.help import router as help_router
from handlers.start import router as start_router
from handlers.stats import router as stats_router
from utils.database import init_database
from utils.errors import router as error_router
from utils.logger import logger, setup_logging
from utils.session_state import session_states


async def main() -> None:
    setup_logging()

    logger.info("Starting application...")

    validate_config()
    init_database()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(generator_router)
    dp.include_router(account_router)
    dp.include_router(stats_router)

    dp.include_router(error_router)

    cleanup_task = asyncio.create_task(
        session_states.cleanup_loop()
    )

    logger.info("Bot handlers registered.")
    logger.info("Starting Telegram polling...")

    try:
        await dp.start_polling(bot)
    finally:
        logger.info("Stopping bot...")

        cleanup_task.cancel()

        try:
            await cleanup_task
        except asyncio.CancelledError:
            pass

        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception:
        logger.exception("Fatal application error.")
        raise
