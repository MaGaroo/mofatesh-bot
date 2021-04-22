import os
import pathlib

import config
from db import Course


class Subscriber:
    @staticmethod
    def list():
        return list(map(
            lambda chat_id: Subscriber(chat_id),
            os.listdir(config.LISTENERS_DIR),
        ))

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)
        self.init_fs()

    def list_courses(self):
        return os.listdir(self.courses_dir)

    def init_fs(self):
        os.makedirs(self.courses_dir, exist_ok=True)

    def listen_to(self, course_code):
        pathlib.Path(self.get_course_file(course_code)).touch()
        os.makedirs(Course(course_code).data_dir, exist_ok=True)

    def deafen_to(self, course_code):
        address = self.get_course_file(course_code)
        if os.path.exists(address):
            os.remove(address)

    def get_updates(self):
        todo_messages = {}
        for course_code in self.list_courses():
            my_course_file = self.get_course_file(course_code)
            with open(my_course_file, 'r+') as f:
                published_indices = set(
                    [
                        line[:-1] if line and line[-1] == '\n' else line
                        for line in f.readlines()
                    ]
                )

            course = Course(course_code)
            course_dir = course.messages_dir
            all_indices = course.messages_list

            print(all_indices)

            todo_indices = [idx for idx in all_indices if idx not in published_indices]
            if todo_indices:
                todo_messages[course_code] = list()
                for idx in todo_indices:
                    message_address = os.path.join(course_dir, idx)
                    with open(message_address, 'r') as message_file:
                        todo_messages[course_code].append((idx, message_file.read()))
        return todo_messages

    def sent_update(self, course_code, msg_id):
        my_course_file = self.get_course_file(course_code)
        with open(my_course_file, 'a+') as f:
            f.write(f'{msg_id}\n')

    def get_course_file(self, course_code):
        return os.path.join(self.courses_dir, course_code)

    @property
    def courses_dir(self):
        return os.path.join(config.LISTENERS_DIR, self.chat_id)
