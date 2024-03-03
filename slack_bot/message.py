from logging import Logger
from typing import Optional

from slack_bolt import Say


def handle_message(event: Optional[dict[str, any]], say: Say, logger: Logger):
    logger.info(event)
    reply_text = "Hai Juga!"
    say(text=f"{reply_text}")
