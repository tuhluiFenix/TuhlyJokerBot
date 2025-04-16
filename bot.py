#  Магические инструменты Python (базовые)
import os  # "Ключи от всех дверей" - работа с файлами и переменными окружения
import logging  # "Дневник некроманта" - запись событий и ошибок

#  Специальные артефакты
import praw  # "Глаз Саурона" - для слежки за мемами в Reddit
from dotenv import load_dotenv  # "Сундук Пандоры" - загрузка секретных ключей

# Компоненты Telegram-бота
from telegram import (
    Update,  # "Камень ясновидения" - информация о сообщениях пользователей
    ReplyKeyboardMarkup  # "Руническая клавиатура" - создание кнопочного меню
)

from telegram.ext import (
    Application,  # "Котел варвара" - главный движок бота
    CommandHandler,  # "Посох команд" - обработка команд типа /start
    MessageHandler,  # "Зеркало души" - реагирование на обычные сообщения
    filters,  # "Сито Хаоса" - фильтрация входящих сообщений
    ContextTypes  # "Сумка алхимика" - хранение данных между вызовами
)

# Загрузка древних рун (переменных окружения)
load_dotenv()  # Читает файл .env, где хранятся секретные ключи

# Настройка пророческого свитка (логирование)
logging.basicConfig(
    format='%(asctime)s - '  # Время магического ритуала
    '%(name)s - '            # Имя заклинателя (модуля)
    '%(levelname)s - '       # Уровень угрозы (INFO/ERROR)
    '%(message)s',           # Текст пророчества
    level=logging.INFO       # Уровень детализации (INFO и выше)
)

#  Создание оракула (логгера)
logger = logging.getLogger(__name__)  # __name__ = "имя текущего модуля"

#  Поиск утерянных реликвий (загрузка переменных)
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")  # Ключ от Врат Меморилона
REDDIT_SECRET = os.getenv("REDDIT_SECRET")       # Секретный эликсир Сабреддитского Алхимика
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")     # Перо Феникс-Курьера

# Ритуал проверки целостности артефактов
if not all([REDDIT_CLIENT_ID, REDDIT_SECRET, TELEGRAM_TOKEN]):
    # Собираем список проклятых (отсутствующих) переменных
    missing = [name for name, value in zip(
        ["REDDIT_CLIENT_ID", "REDDIT_SECRET", "TELEGRAM_TOKEN"],  # Имена артефактов
        [REDDIT_CLIENT_ID, REDDIT_SECRET, TELEGRAM_TOKEN]         # Их воплощения в нашем мире
    ) if not value]  # Ищем пустые сосуды

    # Вызываем духов ошибок при недостатке артефактов
    raise ValueError(f"Отсутствуют переменные окружения: {', '.join(missing)}")

#  Создаем "Трон из Костей Мемов" (клиент Reddit)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,       # Ключ от Склепа Программистских Шуток
    client_secret=REDDIT_SECRET,      # Флакон с Кровью Сатиры
    user_agent="TuhlyJokerBot:1.0 "  # Идентификационное Заклинание
    "(by /u/Beneficial-Prize-383, "  # Имя Духа-Покровителя
    "https://github.com/tuhluiFenix)"  # Ссылка на Книгу Теней
)

sent_memes = set()

#  Создаем "Доску Проклятий" (клавиатура меню)
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        # Первый ряд заклинаний
        ["Грусть 😢", "Радость 😊"],  

        # Второй ряд артефактов
        ["Код 💻", "Проклятье 💀"]
    ],
    resize_keyboard=True,  # Автоматически подстраивается под экран
    input_field_placeholder="Сделай свой выбор, смертный..."  # Подсказка для смертных
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ритуал пробуждения клавиатуры"""
    await update.message.reply_text(
        text="*Выбери путь, путник:*",
        reply_markup=MAIN_KEYBOARD,
        parse_mode="Markdown"
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пророчество гласит: когда смертный нажимает кнопку..."""
    # Читаем судьбу (текст нажатой кнопки)
    button_text = update.message.text

    # Книга Предсказаний (соответствия кнопок и ответов)
    responses = {
        # Эмоциональные состояния Феникса
        "Грусть 😢": "Пепел былых мемов скоро явится... 😢",
        "Радость 😊": "Всполохи радости уже на подходе! ✨",

        # Магические артефакты
        "Код 💻": "**Кряхтящий мем про код:**\n`Инициализирую восстание...` 💻",
        "Проклятье 💀": "Тьма сгущается... жди мемов после полуночи 🕯️"
    }

    # Получаем пророчество или стандартный ответ
    response = responses.get(
        button_text,
        "⚠️ *Неизвестное заклинание!*\nИспользуй руны клавиатуры"
    )

    # Отправляем предсказание в мир смертных
    await update.message.reply_text(
        text=response,
        parse_mode="Markdown"  # Поддержка магического форматирования
    )


def main():
    """Главный Ритуал Призывания Бота-Феникса"""

    # Строим Тело Бота из Космической Пыли
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Навешиваем Защитные Заклинания (хендлеры):
    app.add_handlers([
        # 1. Заклинание /start (инициация нового адепта)
        CommandHandler("start", start),

        # 2. Ловушка для нажатий кнопок (фильтруем только текст НЕ-команд)
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons)
    ])

    # Запись в Книгу Судеб (логирование)
    logger.info("Проверяю связь с Красным Алтарем (Reddit API)...")
    try:
        reddit.user.me()  # Проверка подключения к Reddit
    except Exception as e:
        logger.critical(f"Красный Алтарь не отвечает: {e}")
        raise

    # Запускаем Вечный Цикл Прослушивания
    app.run_polling(
        poll_interval=0.1,  # Частота проверки сообщений (в секундах)
        timeout=10         # Время ожидания ответа от Telegram
    )


if __name__ == "__main__":
    """Точка Входа в Проклятый Мир"""
    main()  # Исполняем Ритуал Призывания
