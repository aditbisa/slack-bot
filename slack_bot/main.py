import os

from dotenv import load_dotenv
from slack_bolt import App

from slack_bot.app_home import handle_app_home_opened
from slack_bot.message import handle_message

# Envar
load_dotenv()
slack_bot_token = os.getenv("SLACK_BOT_TOKEN", "")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET", "")
slack_port = int(os.getenv("SLACK_PORT", 5566))

# Slack Bolt
app = App(token=slack_bot_token, signing_secret=slack_signing_secret)


# Start: Event Handlers ========================================================

app.event("app_home_opened")(handle_app_home_opened)

app.event("message")(handle_message)
app.event("app_mention")(handle_message)

# End: Event Handlers ==========================================================


# Slack.startup()
app.start(port=slack_port)
