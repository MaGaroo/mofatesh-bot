import time
import threading

import config
from collector.crawler import Crawler


def main():
    while True:
        crawler = Crawler()
        threading.Thread(target=crawler.crawl).start()
        time.sleep(config.COLLECTOR_SLEEP_TIME)
    return 0


if __name__ == '__main__':
    exit(main())
