# TuhlyJokerBot - Бот-Феникс с Проклятыми Мемами

> *"Я восстану из пепла... и принесу тебе мемы!"*  
> — Последние слова предыдущего бота

## Описание
Бот для Telegram, который:
- Достает свежие мемы из r/ProgrammerHumor  
- Реагирует на разные эмоции пользователя  
- Автоматически восстанавливается после сбоев  

## Установка
```bash
# 1. Клонируйте репозиторий
git clone https://github.com/tuhluiFenix/tuhly_joker_bot.git
cd tuhly_joker_bot

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Создайте файл .env с вашими ключами
echo "TELEGRAM_TOKEN=ваш_токен" > .env
echo "REDDIT_CLIENT_ID=ваш_id" >> .env
echo "REDDIT_SECRET=ваш_секрет" >> .env