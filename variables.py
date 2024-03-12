# https://github.com/dilshadhasnain07/Membot


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 24683098  # Get this value from my.telegram.org/apps
    API_HASH = "e4055cd239464e50e69bd73057c05dd3"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002074034670
    MESSAGE_DUMP = -1002074034670

    

    # Support chat and support ID
    SUPPORT_CHAT = "ANIME_FOREST_07"
    SUPPORT_ID = -1001629811868


    # Bot token
    TOKEN = "6958105710:AAEAMlWeHd5RYwMvwBrPtBfWC0Xjmh6phOI"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6346273488
    # <=======================================================================================================>
