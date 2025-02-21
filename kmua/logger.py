import sys
from datetime import timedelta

from loguru import logger

from kmua.config import settings

logger.remove()
logger.add(
    "logs/kmua.log",
    rotation="04:00",
    enqueue=True,
    encoding="utf-8",
    level="TRACE",
    retention=timedelta(days=settings.get("log_retention_days", 30)),
)

logger.add(sys.stdout, level=settings.get("log_level", "INFO"))
