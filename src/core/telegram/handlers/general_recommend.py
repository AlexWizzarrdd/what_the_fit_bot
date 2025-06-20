from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from states import GENERAL_RECOMMEND, MENU_CHOICE
from utils.navigation import return_to_main_menu

RECOMMEND_OPTIONS = [
    "Тренды сезона",
    "Микро-бренды",
    "Цветовые сочетания",
    "Что-то необычное",
]


async def general_recommend_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[opt] for opt in RECOMMEND_OPTIONS]
    keyboard.append(["Вернуться в меню"])  # ← добавляем кнопку

    await update.message.reply_text(
        "Что тебе интересно:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
    return GENERAL_RECOMMEND


async def handle_general_recommend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    if choice == "Вернуться в меню":
        return await return_to_main_menu(update, context)
    if choice == "Подобрать заново":
        return await general_recommend_entry(update, context)

    await update.message.reply_text("Обрабатываю запрос...")

    await update.message.reply_text(
        f"Вот рекомендации по теме «{choice}» 🌟\n\n"
        "- Совет 1\n"
        "- Совет 2\n"
        "- Совет 3",
        reply_markup=ReplyKeyboardMarkup(
            [["Подобрать заново"], ["Вернуться в меню"]], resize_keyboard=True
        ),
    )
    return GENERAL_RECOMMEND
