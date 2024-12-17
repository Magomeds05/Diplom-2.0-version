import texts.text

async def ban_message(update):
    await update.answer(texts.text.ban, parse_mode='HTML')


async def ban_callbackquery(update):
    await update.message.answer(texts.text.ban, parse_mode='HTML')
    await update.answer()