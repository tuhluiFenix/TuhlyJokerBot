'''import logging
import asyncpraw
import asyncio
import os

logger = logging.getLogger(__name__)




            

async def fetch_memes():
    # Инициализация клиента внутри async-функции
    async with asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent="TuhlyJokerBot:1.0 "
                       "(by /u/Beneficial-Prize-383, "
                       "https://github.com/tuhluiFenix)"
    ) as reddit:  # Автоматическое закрытие соединения
        
        subreddit = await reddit.subreddit("wholesomememes", fetch=True)
        async for submission in subreddit.hot(limit=10):
            print(f"{submission.title}\nURL: {submission.url}\n")

async def main():
    await fetch_memes()

if __name__ == "__main__":
    # Настройка логгирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Запуск асинхронного кода
    asyncio.run(main())'''