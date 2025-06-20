import os
import sys
from telegram import Update, ReplyKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes
from states import GENERAL_RECOMMEND, MENU_CHOICE, GENDER_SELECT
from utils.navigation import return_to_main_menu
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Путь к src/media
BASE_DIR = Path(__file__).resolve().parents[1] / "media" / "male"

RECOMMEND_OPTIONS = [
    "Тренды сезона",
    "Микро-бренды",
    "Цветовые сочетания",
    "Что-то необычное",
]

GENDER_OPTIONS = ["Мужской", "Женский"]

RECOMMENDATION_DATA = {
    "Тренды сезона": {
        "Мужской": [
            {
                "text": "🧥 Совет 1: Лёгкая рубашка / поло + летние шорты",
                "description": (
                    "Носибельный «дачный-городской» вариант на +20 … +30 °C.\n\n"
                    "Ткань: лен или тонкий хлопок дышат и не мнутся.\n"
                    "Длина шорт: до колена или чуть выше — выглядит аккуратно и не «подростково».\n"
                    "Обувь: белые кеды, мокасины, либо лёгкие парусиновые эспадрильи.\n"
                    "Фишка сезона: неброский аксессуар (плетёный браслет, часы с коричневым ремешком) вместо крупных логотипов."
                ),
                "photos": ["trends1_1.jpg", "trends1_2.jpg"],
            },
            {
                "text": "👖 Совет 2: Смарт-кэжуал: поло + чиносы",
                "description": (
                    "Рабочие будни без галстука, свидание в кофейне или прогулка по центру.\n\n"
                    "Крой поло: слегка приталенный, воротник без «стойки», рукав до середины бицепса.\n"
                    "Чиносы: плотность 220-260 г/м², средняя посадка, длина – до косточки.\n"
                    "Цветовая схема: базовые тона (беж, олива, темно-синий) легко сочетаются между собой.\n"
                    "Обувь: кожаные кеды, лоферы, либо дерби на тонкой подошве."
                ),
                "photos": ["trends2_1.jpg", "trends2_2.jpg", "trends2_3.jpg"],
            },
            {
                "text": "🎩 Совет 3: Нормкор / Gorpcore: карго-брюки + тех куртка",
                "description": (
                    "Прагматичный уличный образ для межсезонья и активных выходных.\n\n"
                    "Карго: свободный прямой крой, матовый хлопок или смесовый рип-стоп.\n"
                    "Верх: софтшелл, лёгкий пуховик или флисовый топ в тёмно-серых/хаки оттенках.\n"
                    "Аксессуары: кросс-боди стропа, бейсболка без броских надписей.\n"
                    "Обувь: трейл-кроссовки или хайкеры; подойдут и классические «New Balance» 574/550."
                ),
                "photos": ["trends3_1.jpg", "trends3_2.jpg", "trends3_3.jpg"],
            },
        ]
    }
}


async def general_recommend_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[gender] for gender in GENDER_OPTIONS]
    keyboard.append(["Вернуться в меню"])

    await update.message.reply_text(
        "Кого стилизуем? 👤",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
    return GENDER_SELECT


async def handle_gender_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gender = update.message.text

    if gender == "Вернуться в меню":
        return await return_to_main_menu(update, context)

    context.user_data["gender"] = gender
    return await return_to_recommend_options(update, context)


async def return_to_recommend_options(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    keyboard = [[opt] for opt in RECOMMEND_OPTIONS]
    keyboard.append(["Подобрать заново"])
    keyboard.append(["Вернуться в меню"])

    gender = context.user_data.get("gender", "пользователя").lower()

    await update.message.reply_text(
        f"Отлично! Показываю рекомендации для: *{gender}*.\nЧто тебе интересно?",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
    return GENERAL_RECOMMEND


async def handle_general_recommend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    if choice == "Вернуться в меню":
        return await return_to_main_menu(update, context)
    if choice == "Подобрать заново":
        return await return_to_recommend_options(update, context)

    gender = context.user_data.get("gender")

    await update.message.reply_text("Обрабатываю запрос...")

    tips = RECOMMENDATION_DATA.get(choice, {}).get(gender)

    if not tips:
        await update.message.reply_text("Пока нет рекомендаций для этой категории.")
        return GENERAL_RECOMMEND

    for tip in tips:
        await update.message.reply_text(f"{tip['text']}\n\n{tip['description']}")
        photos = tip.get("photos", [])

        media_paths = [BASE_DIR / p for p in photos if (BASE_DIR / p).exists()]

        if not media_paths:
            await update.message.reply_text("⚠️ Ни одного изображения не найдено.")
            continue

        if len(media_paths) > 1:
            media = [InputMediaPhoto(open(p, "rb")) for p in media_paths]
            await update.message.reply_media_group(media)
        else:
            with open(media_paths[0], "rb") as photo:
                await update.message.reply_photo(photo)

    await update.message.reply_text(
        "Хочешь посмотреть что-то ещё?",
        reply_markup=ReplyKeyboardMarkup(
            [["Подобрать заново"], ["Вернуться в меню"]],
            resize_keyboard=True,
        ),
    )
    return GENERAL_RECOMMEND
