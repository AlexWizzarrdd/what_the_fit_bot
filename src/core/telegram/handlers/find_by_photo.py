import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from states import FIND_PHOTO
from utils.navigation import return_to_main_menu


async def find_by_photo_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пожалуйста, отправь мне фото")
    return FIND_PHOTO


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Если пришёл текст, проверим на команду возврата
    if update.message.text == "Вернуться в меню":
        return await return_to_main_menu(update, context)

    # Если пришло не фото — сообщаем об этом
    if not update.message.photo:
        await update.message.reply_text("Пожалуйста, отправь именно фото.")
        return FIND_PHOTO

    await update.message.reply_text("Обрабатываю фото...")

    await update.message.reply_text(
        "Вот что я нашёл:\n\n"
        "👕 Название: Белая футболка\n"
        "⭐ Оценка: 4.8 / 5\n"
        "💰 Цена: 2 990 ₽\n"
        "🔗 [Ссылка](https://example.com)",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(
            [["Загрузить ещё"], ["Вернуться в меню"]],
            resize_keyboard=True,
        ),
    )

    return FIND_PHOTO
