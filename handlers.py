from telegram import Update
from telegram.ext import ContextTypes
from keyboards import MAIN_KEYBOARD
from clients.reddit import RedditClient
import os
import mimetypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="*Выбери путь, путник:*",
        reply_markup=MAIN_KEYBOARD,
        parse_mode="Markdown"
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button_text = update.message.text

    if button_text == "Радость 😊":
        reddit = RedditClient(
            os.getenv("REDDIT_CLIENT_ID"),
            os.getenv("REDDIT_SECRET")
        )

        memes = reddit.get_happy_memes(limit=5)

        if not memes:
            await update.message.reply_text("Не удалось найти радостные мемы 😢")
            return

        for meme in memes:
            try:
                url = meme['url']
                mime_type, _ = mimetypes.guess_type(url)

                if mime_type and mime_type.startswith('image/'):
                    if mime_type.endswith('gif'):
                        await update.message.reply_animation(
                            animation=url,
                            caption=f"{meme['title']}\n(с r/{meme['subreddit']})"
                        )
                    else:
                        await update.message.reply_photo(
                            photo=url,
                            caption=f"{meme['title']}\n(с r/{meme['subreddit']})"
                        )
                elif url.endswith(('.mp4', '.webm')):
                    await update.message.reply_video(
                        video=url,
                        caption=f"{meme['title']}\n(с r/{meme['subreddit']})"
                    )
                else:
                    await update.message.reply_text(
                        f"{meme['title']}\n(с r/{meme['subreddit']})\n{url}"
                    )
                break  # Отправляем только один мем

            except Exception as e:
                print(f"Ошибка при отправке мема: {e}")
                continue

        return  # Прерываем дальнейшую обработку для кнопки "Радость"

    # Обработка остальных кнопок
    responses = {
        "Грусть 😢": "Пепел былых мемов скоро явится... 😢",
        "Код 💻": "**Кряхтящий мем про код:**\n`Инициализирую восстание...` 💻",
        "Проклятье 💀": "Тьма сгущается... жди мемов после полуночи 🕯️"
    }

    await update.message.reply_text(
        text=responses.get(button_text, "⚠️ Неизвестное заклинание!"),
        parse_mode="Markdown"
    )
