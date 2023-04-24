from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
    filters,
)

from .callbacks import (
    chat_migration,
    clear_chat_quote,
    clear_chat_quote_ask,
    clear_chat_quote_cancel,
    clear_user_data,
    del_quote,
    inline_query_quote,
    interact,
    quote,
    random_quote,
    set_quote_probability,
    start,
    title,
    user_data_manage,
)
from .filters import interact_filter, start_filter
from .logger import logger

start_handler = CommandHandler("start", start, filters=start_filter)
chat_migration_handler = MessageHandler(filters.StatusUpdate.MIGRATE, chat_migration)
title_handler = CommandHandler("t", title)
quote_handler = CommandHandler("q", quote)
set_quote_probability_handler = CommandHandler("setqp", set_quote_probability)
random_quote_handler = MessageHandler(~filters.COMMAND, random_quote)
del_quote_handler = CommandHandler("d", del_quote)
clear_chat_quote_ask_handler = CommandHandler("c", clear_chat_quote_ask)
clear_chat_quote_handler = CallbackQueryHandler(
    clear_chat_quote, pattern="clear_chat_quote"
)
clear_chat_quote_cancel_handler = CallbackQueryHandler(
    clear_chat_quote_cancel, pattern="cancel_clear_chat_quote"
)
interact_handler = MessageHandler(filters=interact_filter, callback=interact)
inline_query_handler = InlineQueryHandler(inline_query_quote)
user_data_manage_handler = CallbackQueryHandler(
    user_data_manage, pattern="user_data_manage"
)
clear_user_data_handler = CallbackQueryHandler(
    clear_user_data, pattern="clear_user_data"
)
handlers = [
    start_handler,
    chat_migration_handler,
    title_handler,
    quote_handler,
    set_quote_probability_handler,
    del_quote_handler,
    clear_chat_quote_ask_handler,
    clear_chat_quote_handler,
    clear_chat_quote_cancel_handler,
    interact_handler,
    random_quote_handler,
    inline_query_handler,
    user_data_manage_handler,
    clear_user_data_handler,
]


async def on_error(update: object | None, context: CallbackContext):
    logger.error(f"在该更新发生错误 {update}\n\n错误信息\n{context.error}")
