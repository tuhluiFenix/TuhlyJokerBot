import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.logging import setup_logging
from config.env import load_and_validate
from clients.reddit import RedditClient
from handlers import start, handle_buttons


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        # Загрузка конфигурации
        load_and_validate(
            ['REDDIT_CLIENT_ID', 'REDDIT_SECRET', 'TELEGRAM_TOKEN'])

        # Инициализация клиентов
        RedditClient(
            os.getenv("REDDIT_CLIENT_ID"),
            os.getenv("REDDIT_SECRET")
        )

        # Запуск бота
        app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, handle_buttons))

        logger.info("Бот запущен")
        app.run_polling()

    except Exception as e:
        logger.critical(f"Ошибка: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
