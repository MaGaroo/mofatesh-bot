import os

import config
from collector.page import Page
from collector.page_crawler import HomePageCrawler, AssignmentsPageCrawler


class Course:
    @staticmethod
    def list():
        return os.listdir(config.COURSES_DIR)

    def __init__(self, code):
        self.code = code

    def get_pages(self):
        return [
            Page('home', HomePageCrawler(self.home_url)),
            Page('assign', AssignmentsPageCrawler(self.assignments_url)),
        ]

    def update_messages(self, channel, messages):
        channel_dir = self.get_channel_dir(channel)
        for idx, msg in enumerate(messages):
            print('Update', self.code, channel, idx)
            msg_file_name = os.path.join(channel_dir, str(idx))
            with open(msg_file_name, 'w') as msg_file:
                msg_file.write(msg)

    def get_channel_dir(self, channel):
        address = os.path.join(self.messages_dir, channel)
        os.makedirs(address, exist_ok=True)
        return address

    @property
    def channels_list(self):
        return os.listdir(self.messages_dir)

    @property
    def messages_list(self):
        messages = []
        for channel in self.channels_list:
            indices = os.listdir(self.get_channel_dir(channel))
            indices.sort(key=lambda x: int(x))
            for idx in indices:
                messages.append(f'{channel}/{idx}')
        return messages

    @property
    def url_code(self):
        return self.code.replace('_', '/')

    @property
    def home_url(self):
        return f'http://ce.sharif.edu/courses/{self.url_code}/index.php'

    @property
    def assignments_url(self):
        return f'http://ce.sharif.edu/courses/{self.url_code}/index.php' \
               f'/section/assignments/file/assignments'

    @property
    def data_dir(self):
        return os.path.join(config.COURSES_DIR, self.code)

    @property
    def messages_dir(self):
        return os.path.join(self.data_dir, 'messages')
