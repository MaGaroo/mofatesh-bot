import time

import config
from collector.crawler import Crawler


def main():
    while True:
        crawler = Crawler()
        crawler.crawl()
        time.sleep(config.COLLECTOR_SLEEP_TIME)


if __name__ == '__main__':
    exit(main())
