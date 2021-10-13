from config import ALLOWED_COURSES

MARKDOWN_ESCAPE_CHARS = '|-.(!)#_=*'


def is_valid_course_code(code):
    return code in ALLOWED_COURSES


def escape_message(msg):
    for char in MARKDOWN_ESCAPE_CHARS:
        msg = msg.replace(char, f'\\{char}')
    return msg
