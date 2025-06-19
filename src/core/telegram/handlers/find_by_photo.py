import sys
import os
import tempfile

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

max_products_to_send = 2

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from states import FIND_PHOTO
from utils.navigation import return_to_main_menu

from core.task_pool.pool import pool

async def find_by_photo_entry(
    update: Update,
    _: ContextTypes.DEFAULT_TYPE
):
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

    temp_file_path = os.path.join(
        tempfile.gettempdir(),
        f"{update.message.photo[-1].file_id}.jpg"
    )
    file_handler = await context.bot.get_file(update.message.photo[-1].file_id)
    _ = await file_handler.download_to_drive(custom_path=temp_file_path)

    information = pool.handle(temp_file_path)
    if information == None:
        await update.message.reply_text(
            "Система перегружена запросами, попробуйте позже",
            parse_mode="Markdown",
        )
        return FIND_PHOTO
    
    to_send = min(len(information), max_products_to_send)
    if to_send == 0:
        await update.message.reply_text(
            "Я не смог найти одежду на этой фотографии",
            parse_mode="Markdown",
        )
        return FIND_PHOTO
    
    keys = list(information.keys())

    for i in range(to_send):
        card = information[keys[i]]

        if (card == None or
            card["_Product__name"] == None or
            card["_Product__review_rating"] == None or
            card["_Product__price"] == None or
            card["_Product__link"] == None or
            card["_Product__image_path"] == None):

            await update.message.reply_text(
                "Произошла ошибка, попробуйте позже",
                parse_mode="Markdown",
            )

            return FIND_PHOTO
        
        try:
            photo = open(card["_Product__image_path"], 'rb')
        except:
            await update.message.reply_text(
                "Произошла ошибка, попробуйте позже",
                parse_mode="Markdown",
            )
            return FIND_PHOTO

        await update.message.reply_photo(
            photo=photo,
            caption=f"\
👕 {card["_Product__name"]}\n\
⭐ Оценка: {card["_Product__review_rating"]} / 5\n\
💰 Цена: {card["_Product__price"]} ₽\n\
🔗 [Ссылка]({card["_Product__link"]})\
",
            parse_mode="Markdown",
            reply_markup= ReplyKeyboardMarkup(
                [["Загрузить ещё"], ["Вернуться в меню"]],
                resize_keyboard=True,
            )
        )

    return FIND_PHOTO
