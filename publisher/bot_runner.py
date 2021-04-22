import time

import telegram.error
from telegram import Bot, ParseMode
from telegram.ext import Updater, CommandHandler

import config
from db.subscriber import Subscriber
from publisher import handlers


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
                            bot.send_message(
                                subscriber.chat_id,
                                msg,
                                parse_mode=ParseMode.HTML,
                            )
                            subscriber.sent_update(course, idx)
                        except telegram.error.TimedOut as e:
                            print('Ah timeout...')
                        except Exception as e:
                            e.print_exc()

            time.sleep(config.BOT_SLEEP_TIME)
