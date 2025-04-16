import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    """Настройка логирования"""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            RotatingFileHandler(
                    "bot.log",
                    maxBytes=5*1024*1024,
                    backupCount=3
                    ),
            logging.StreamHandler()
        ]
    )
