from db import Course


class CourseCrawler:
    def __init__(self, course_code):
        self.course = Course(course_code)

    def crawl(self):
        pages = self.course.get_pages()
        for page in pages:
            messages = page.crawler.get_messages()
            self.course.update_messages(page.title, messages)
