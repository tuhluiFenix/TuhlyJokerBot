import praw
import os


class RedditClient:
    def __init__(self):
        self.client = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_SECRET"),
            user_agent="TuhlyJokerBot:1.0 "
                       "(by /u/Beneficial-Prize-383, "
                       "https://github.com/tuhluiFenix)"
        )

    def get_memes(self, subreddit: str, limit=10):
        """Получение мемов с указанного сабреддита"""
        return list(self.client.subreddit(subreddit).hot(limit=limit))