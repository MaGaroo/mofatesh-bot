ESCAPE_CHARS = '|-.(!)#_=*'


def is_valid_course_code(code):
    return code == '99-00_2_ce242-1'


def escape_message(msg):
    for char in ESCAPE_CHARS:
        msg = msg.replace(char, f'\\{char}')
    return msg
