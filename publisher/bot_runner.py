import time

from telegram import Bot, ParseMode
from telegram.ext import Updater, CommandHandler
import telegram.error

from db.subscriber import Subscriber
from publisher import handlers, utils


class BotRunner:
    def __init__(self, token):
        self.token = token

    def run(self):
        updater = Updater(self.token)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', handlers.start_command_handler))
        dispatcher.add_handler(CommandHandler('listen', handlers.listen_command_handler))
        dispatcher.add_handler(CommandHandler('deafen', handlers.deafen_command_handler))
        dispatcher.add_handler(CommandHandler('help', handlers.help_command_handler))

        updater.start_polling()

        bot = Bot(self.token)
        while True:
            for subscriber in Subscriber.list():
                updates = subscriber.get_updates()
                for course, updates in updates.items():
                    for idx, msg in updates:
                        try:
                            bot.send_message(subscriber.chat_id, utils.escape_message(msg), parse_mode=ParseMode.MARKDOWN_V2)
                            subscriber.sent_update(course, idx)
                        except telegram.error.TimedOut as e:
                            print('Ah timeout...')
                        except Exception as e:
                            e.print_exc()

            time.sleep(10)
