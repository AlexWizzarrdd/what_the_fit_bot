import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    ConversationHandler,
)

from handlers.pick_by_style import pick_style_entry, style_select, style_detail
from handlers.find_by_photo import find_by_photo_entry, handle_photo
from handlers.general_recommend import (
    general_recommend_entry,
    handle_gender_selection,
    handle_general_recommend,  # ← обязательно импортируем
)

from states import (
    FIND_PHOTO,
    STYLE_SELECT,
    STYLE_DETAIL,
    MENU_CHOICE,
    GENERAL_RECOMMEND,
    GENDER_SELECT,
)

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("ACCESS_TOKEN")
if not TOKEN:
    raise ValueError("ACCESS_TOKEN не найден в .env")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logo_path = os.path.join("media", "logo.png")
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as photo:
            await update.message.reply_photo(photo)

    await update.message.reply_text(
        """👋 *Привет!*

В этом боте ты найдёшь всё, чтобы выглядеть стильно и чувствовать себя уверенно:

🔎 Загрузишь фото — и я найду похожие вещи на маркетплейсах  
🧥 Подберу образы, которые подойдут именно тебе  
🎨 Дам рекомендации по цветотипу, чтобы подчеркнуть твою красоту

*Начнём?* ✨""",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup([["🚀 Поехали"]], resize_keyboard=True),
    )
    return MENU_CHOICE


# Обработка главного меню и всех общих команд
async def main_menu_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in ["🚀 Поехали", "Вернуться в меню"]:
        keyboard = [
            ["Найти по фото"],
            ["🔒 Подбор по стилю"],
            ["Общие рекомендации"],
        ]
        await update.message.reply_text(
            "Что хочешь попробовать?",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
        )
        return MENU_CHOICE

    elif text in ["Загрузить ещё", "Найти по фото"]:
        return await find_by_photo_entry(update, context)

    elif text == "🔒 Подбор по стилю":
        await update.message.reply_text("❌ Этот раздел пока недоступен.")
        return MENU_CHOICE

    elif text == "Общие рекомендации":
        return await general_recommend_entry(update, context)  # ← корректный вызов

    else:
        await update.message.reply_text("Я не понял. Пожалуйста, выбери пункт из меню.")
        return MENU_CHOICE


# MAIN
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU_CHOICE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_router),
            ],
            FIND_PHOTO: [
                MessageHandler(filters.PHOTO, handle_photo),
                MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_router),
            ],
            STYLE_SELECT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, style_select),
            ],
            STYLE_DETAIL: [],
            GENDER_SELECT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, handle_gender_selection
                ),
            ],
            GENERAL_RECOMMEND: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, handle_general_recommend
                ),
            ],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
