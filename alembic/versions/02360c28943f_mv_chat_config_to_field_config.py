"""mv chat config to field config

Revision ID: 02360c28943f
Revises: 5ad3da643ecc
Create Date: 2024-07-13 22:29:16.220883

"""

import json
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "02360c28943f"
down_revision: Union[str, None] = "5ad3da643ecc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.add_column("chat_data", sa.Column("config", sa.JSON(), nullable=True))
    except Exception:
        print("column config already")
    # migrate data
    try:
        print("migrating data")
        connection = op.get_bind()
        chats = connection.execute(
            sa.text(
                "SELECT id, waifu_disabled, delete_events_enabled, unpin_channel_pin_enabled, title_permissions, greet, quote_probability, message_search_enabled FROM chat_data"
            )
        ).fetchall()
        for chat in chats:
            config = {
                "waifu_enabled": chat.waifu_disabled != 1,
                "delete_events_enabled": chat.delete_events_enabled == 1,
                "unpin_channel_pin_enabled": chat.unpin_channel_pin_enabled == 1,
                "title_permissions": json.loads(chat.title_permissions or "\{\}"),
                "greeting": chat.greet,
                "quote_probability": chat.quote_probability or 0.001,
                "message_search_enabled": chat.message_search_enabled == 1,
            }
            connection.execute(
                sa.text("UPDATE chat_data SET config = :config WHERE id = :id"),
                {"config": json.dumps(config, ensure_ascii=False), "id": chat.id},
            )
        print(f"migrated {len(chats)} chats")
    except Exception as e:
        print(e)
    op.drop_column("chat_data", "unpin_channel_pin_enabled")
    op.drop_column("chat_data", "waifu_disabled")
    op.drop_column("chat_data", "title_permissions")
    op.drop_column("chat_data", "delete_events_enabled")
    op.drop_column("chat_data", "message_search_enabled")
    op.drop_column("chat_data", "greet")
    op.drop_column("chat_data", "quote_probability")

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chat_data", sa.Column("message_search_enabled", sa.BOOLEAN(), nullable=True)
    )
    op.add_column(
        "chat_data", sa.Column("delete_events_enabled", sa.BOOLEAN(), nullable=True)
    )
    op.add_column(
        "chat_data", sa.Column("quote_probability", sa.FLOAT(), nullable=True)
    )
    op.add_column(
        "chat_data", sa.Column("title_permissions", sqlite.JSON(), nullable=True)
    )
    op.add_column("chat_data", sa.Column("waifu_disabled", sa.BOOLEAN(), nullable=True))
    op.add_column(
        "chat_data", sa.Column("unpin_channel_pin_enabled", sa.BOOLEAN(), nullable=True)
    )
    op.add_column("chat_data", sa.Column("greet", sa.VARCHAR(), nullable=True))

    # migrate data
    connection = op.get_bind()
    chats = connection.execute(sa.text("SELECT id, config FROM chat_data")).fetchall()
    for chat in chats:
        config = json.loads(chat.config)
        connection.execute(
            sa.text(
                "UPDATE chat_data SET waifu_disabled = :waifu_disabled, delete_events_enabled = :delete_events_enabled, unpin_channel_pin_enabled = :unpin_channel_pin_enabled, title_permissions = :title_permissions, greet = :greet, quote_probability = :quote_probability, message_search_enabled = :message_search_enabled WHERE id = :id",
            ),
            {
                "waifu_disabled": not config["waifu_enabled"],
                "delete_events_enabled": config["delete_events_enabled"],
                "unpin_channel_pin_enabled": config["unpin_channel_pin_enabled"],
                "title_permissions": json.dumps(config["title_permissions"]),
                "greet": config["greeting"],
                "quote_probability": config["quote_probability"],
                "message_search_enabled": config["message_search_enabled"],
                "id": chat.id,
            },
        )

    op.drop_column("chat_data", "config")
    # ### end Alembic commands ###
