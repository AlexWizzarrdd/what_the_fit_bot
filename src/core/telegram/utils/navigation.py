from telegram import ReplyKeyboardMarkup

MAIN_MENU = [["Найти по фото"], ["🔒Подбор по стилю"], ["Общие рекомендации"]]


async def return_to_main_menu(update, context):
    await context.application.bot.send_message(
        chat_id=update.effective_chat.id,
        text="В этом боте ты найдешь всё, чтобы выглядеть стильно!\n\nЧто хочешь попробовать?",
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True),
    )
    return 3  # MENU_CHOICE
