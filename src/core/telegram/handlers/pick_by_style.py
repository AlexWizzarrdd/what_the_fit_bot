from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from states import STYLE_SELECT, STYLE_DETAIL, MENU_CHOICE
from utils.navigation import return_to_main_menu

STYLES = ["Классика", "Casual", "Streetwear", "Old Money", "Спорт"]
SUBSTYLE_CHOICES = ["Повседневно", "На выход", "Всё подряд"]


async def pick_style_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[s] for s in STYLES]
    keyboard.append(["Вернуться в меню"])  # Добавляем кнопку возврата
    await update.message.reply_text(
        "Выбери стиль:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
    return STYLE_SELECT


async def style_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    if choice == "Вернуться в меню":
        return await return_to_main_menu(update, context)
    if choice == "Подобрать заново":
        return await pick_style_entry(update, context)

    context.user_data["style"] = choice

    if choice in ["Casual", "Streetwear"]:
        keyboard = [[s] for s in SUBSTYLE_CHOICES]
        keyboard.append(["Вернуться в меню"])  # Добавляем кнопку и сюда
        await update.message.reply_text(
            "На каждый день или что-то особое?",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
        )
        return STYLE_DETAIL
    else:
        return await send_style_results(update, context)


async def style_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    if choice == "Вернуться в меню":
        return await return_to_main_menu(update, context)
    if choice == "Подобрать заново":
        return await pick_style_entry(update, context)

    context.user_data["substyle"] = choice
    return await send_style_results(update, context)


async def send_style_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    style = context.user_data.get("style")
    sub = context.user_data.get("substyle", "")

    await update.message.reply_text("Обрабатываю запрос...")

    await update.message.reply_text(
        f"Вот твоя подборка стиля: {style} {f'({sub})' if sub else ''} 👕\n"
        "- Белая рубашка\n"
        "- Синие джинсы\n"
        "- Кроссовки\n",
        reply_markup=ReplyKeyboardMarkup(
            [["Подобрать заново"], ["Вернуться в меню"]],
            resize_keyboard=True,
        ),
    )
    return STYLE_SELECT
