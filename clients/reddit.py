import praw
import logging
from typing import List, Dict, Set
import random
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
        self.sent_meme_ids: Set[str] = set()

    def _check_connection(self):
        """Проверка подключения к Reddit"""
        try:
            user = self.client.user.me()
            logger.info(f"Reddit подключен. Юзер: {user}")
        except Exception as e:
            logger.critical(f"Ошибка Reddit: {e}")
            raise

    def get_happy_memes(self) -> List[Dict]:
        """Получает радостные мемы с подходящих сабреддитов"""
        subreddits = ["wholesomememes", "MadeMeSmile", "happy"]
        posts = []

        for sub in subreddits:
            try:
                for post in self.client.subreddit(sub):
                    if (not post.stickied
                        and post.url
                        and post.id not in self.sent_meme_ids):

                        posts.append({
                            "id": post.id,
                            "title": post.title,
                            "url": post.url,
                            "subreddit": sub
                        })
            except Exception as errors:
                print(f"Ошибка при парсинге {sub}: {errors}")

        if not posts:
            return []

        selected_meme = random.choice(posts)
        self.sent_meme_ids.add(selected_meme["id"])
        return [selected_meme]
