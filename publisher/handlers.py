from telegram import ParseMode

from db.subscriber import Subscriber
from publisher import bot_strings, utils


def start_command_handler(update, _):
    update.message.reply_text(bot_strings.TEST_MSG, parse_mode=ParseMode.HTML)
    return
    update.message.reply_text(bot_strings.WELCOME_MESSAGE)


def listen_command_handler(update, _):
    course_code = update.message.text.split('/listen')[1].strip()
    if not utils.is_valid_course_code(course_code):
        update.message.reply_text(bot_strings.INVALID_COURSE)
        return

    subscriber = Subscriber(update.message.chat.id)
    if course_code in subscriber.list_courses():
        update.message.reply_text(bot_strings.ALREADY_A_SUBSCRIBER)
        return

    subscriber.listen_to(course_code)
    update.message.reply_text(bot_strings.OK)


def deafen_command_handler(update, _):
    course_code = update.message.text.split('/deafen')[1].strip()
    subscriber = Subscriber(update.message.chat.id)
    if course_code not in subscriber.list_courses():
        update.message.reply_text(bot_strings.NOT_A_SUBSCRIBE)
    else:
        subscriber.deafen_to(course_code)
        update.message.reply_text(bot_strings.OK)


def help_command_handler(update, _):
    update.message.reply_text(bot_strings.HELP_MESSAGE)
