import time

from collector.crawler import Crawler


def main():
    while True:
        crawler = Crawler()
        crawler.crawl()
        time.sleep(60)


if __name__ == '__main__':
    exit(main())
