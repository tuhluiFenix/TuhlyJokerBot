import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def load_and_validate(required_vars: list[str]):
    """Загрузка и валидация переменных окружения"""
    load_dotenv()

    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        error_msg = f"Отсутствуют переменные: {', '.join(missing)}"
        logger.critical(error_msg)
        raise EnvironmentError(error_msg)
