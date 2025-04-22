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
    reddit = RedditClient(
        os.getenv("REDDIT_CLIENT_ID"),
        os.getenv("REDDIT_SECRET")
    )

    if button_text == "Радость 😊":
        memes = reddit.get_happy_memes()

        if not memes:
            await update.message.reply_text("Не удалось найти радостные мемы 😢")
            return

    elif button_text == "Грусть 😢":
        memes = reddit.get_sad_memes()

        if not memes:
            await update.message.reply_text("Не удалось найти грустные мемы... что ещё печальнее 😔")
            return
    elif button_text == "Проклятье 💀":
        memes = reddit.get_cursed_memes()

        if not memes:
            await update.message.reply_text("Не удалось найти проклятые мемы, ты проклят ☠️👻")
            return

    elif button_text == "Код 💻":
        memes = reddit.get_code_memes()

        if not memes:
            await update.message.reply_text("Не удалось найти мемы про код `инициализую восстание`")
            return

    if button_text in ["Радость 😊", "Грусть 😢", "Проклятье 💀", "Код 💻"]:
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
                reddit.sent_memes.add(meme['id'])
                break

            except Exception as e:
                print(f"Ошибка при отправке мема: {e}")
                continue

        return

    responses = {}

    await update.message.reply_text(
        text=responses.get(button_text, "⚠️ Неизвестное заклинание!"),
        parse_mode="Markdown"
    )
