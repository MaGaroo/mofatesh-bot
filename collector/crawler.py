from collector.course_crawler import CourseCrawler
from db import Course


class Crawler:
    def __init__(self):
        Course.list()

    def crawl(self):
        for course in Course.list():
            cc = CourseCrawler(course)
            cc.crawl()
