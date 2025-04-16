import praw
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class RedditClient:
    def __init__(self, client_id: str, client_secret: str):
        self.client = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="TuhlyJokerBot:1.0 "
                       "(by /u/Beneficial-Prize-383, "
                       "https://github.com/tuhluiFenix)"
        )
        self._check_connection()

    def _check_connection(self):
        """Проверка подключения к Reddit"""
        try:
            user = self.client.user.me()
            logger.info(f"Reddit подключен. Юзер: {user}")
        except Exception as e:
            logger.critical(f"Ошибка Reddit: {e}")
            raise

    def get_happy_memes(self, limit: int = 5) -> List[Dict]:
        """Получает радостные мемы с подходящих сабреддитов"""
        subreddits = ["wholesomememes", "MadeMeSmile", "happy"]
        posts = []

        for sub in subreddits:
            try:
                for post in self.client.subreddit(sub).hot(limit=limit):
                    if not post.stickied and post.url:
                        posts.append({
                            "title": post.title,
                            "url": post.url,
                            "subreddit": sub
                        })
            except Exception as e:
                print(f"Ошибка при парсинге {sub}: {e}")

        return posts
