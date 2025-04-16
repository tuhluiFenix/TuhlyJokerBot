from telegram import ReplyKeyboardMarkup

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        ["Грусть 😢", "Радость 😊"],
        ["Код 💻", "Проклятье 💀"]
    ],
    resize_keyboard=True,
    input_field_placeholder="Сделай свой выбор..."
)
