from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from tbot.handlers import start, echo
from tbot.settings import BOT_TOKEN


def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
