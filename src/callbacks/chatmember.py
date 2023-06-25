from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.ext import (
    ContextTypes,
)

from ..logger import logger


def extract_status_change(chat_member_update: ChatMemberUpdated):
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get(
        "is_member", (None, None)
    )

    if status_change is None:
        return None

    old_status, new_status = status_change
    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    return was_member, is_member


async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tracks the chats the bot is in."""
    result = extract_status_change(update.my_chat_member)
    if result is None:
        return
    was_member, is_member = result

    # Let's check who is responsible for the change
    cause_name = update.effective_user.full_name

    # Handle chat types differently:
    chat = update.effective_chat
    if chat.type == Chat.PRIVATE:
        if not was_member and is_member:
            logger.debug(f"{cause_name} started the bot")

        elif was_member and not is_member:
            logger.debug(f"{cause_name} 拉黑了bot")

    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        if not was_member and is_member:
            logger.debug(f"{cause_name} 将bot添加到群组 {chat.title}")

        elif was_member and not is_member:
            logger.debug(f"{cause_name} 将bot移出群组 {chat.title}")
            context.chat_data.clear()
            logger.debug(f"清除 {chat.title} 数据")

    elif not was_member and is_member:
        logger.debug(f"{cause_name} 将bot添加到频道 {chat.title}")

    elif was_member and not is_member:
        logger.debug(f"{cause_name} 将bot移出频道 {chat.title}")


async def on_member_left(update: Update, context: ContextTypes.DEFAULT_TYPE):
    left_user = update.effective_message.left_chat_member
    logger.debug(f"{left_user.full_name} 退出了群聊 {update.effective_chat.title} ")
    try:
        del context.chat_data["members_data"][left_user.id]
        logger.debug(f"将 {left_user.full_name} 从 {update.effective_chat.title} 数据中移除")
    except KeyError:
        logger.debug(f"{left_user.full_name} 未在 {update.effective_chat.title} 数据中")


async def on_member_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joined_user = update.effective_message.new_chat_members[0]
    logger.debug(f"{joined_user} 加入了群聊 {update.effective_chat.title} ")
    # TODO: greet new member
