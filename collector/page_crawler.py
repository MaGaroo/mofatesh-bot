import urllib.parse

import requests
from bs4 import BeautifulSoup

from collector import utils
from collector.utils import dirty_url_join


class PageCrawler:
    def __init__(self, url):
        self.url = url

    def get_messages(self):
        pass


class HomePageCrawler(PageCrawler):
    def get_messages(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.find('table', attrs={'class': 'headtable'})
        body = list(head.next_siblings)[3].find('tr')
        right = body.findAll('td', recursive=False)[1].find('table')
        rows = right.findAll('tr', recursive=False)[2]
        msgt = rows.find('table').find('td')
        msgs = msgt.findAll('tr', recursive=False)
        msgs = reversed(msgs)
        return list(map(lambda msg: self.parse_message(msg), msgs))

    def parse_message(self, html):
        date = html.find('table', attrs={'class': 'titlebar'}).find('td').text.strip()
        table1 = html.find('table', attrs={'class': 'table1'})
        text = table1.find('td').find('tr').find('td').text.strip()

        return self.render_message(date, text)

    def render_message(self, date, text):
        return f'New announcement | {date}\n' \
               f'\n' \
               f'{text}'


class AssignmentsPageCrawler(PageCrawler):
    def get_messages(self):
        resp = requests.get(self.url)
        self.url = resp.url
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.find('table', attrs={'class': 'headtable'})
        body = list(head.next_siblings)[3].find('tr')
        right = body.findAll('td', recursive=False)[1]
        msgs = right.findAll('table', recursive=False)[1:]
        msgs = reversed(msgs)
        return list(map(lambda msg: self.parse_message(msg), msgs))

    def parse_message(self, html):
        title = html.find('table').find('b').text
        deadline = html.find('table').findAll('b')[1].text.strip()

        table1 = html.find('table', attrs={'class', 'table1'})
        rows = table1.findAll('tr', recursive=False)[1:-1]
        sections = list()
        for row in rows:
            part_name = row.find('b').text.split('\xa0')[-1].strip()
            text = row.find('table').find('td').text.strip()

            link_elems = row.findAll('a')
            links = {}
            for elem in link_elems:
                href = dirty_url_join(self.url, elem['href'])
                links[elem.text.strip()] = href

            sections.append([part_name, text, links])

        return self.render_message(title, deadline, sections)

    def render_message(self, title, deadline, sections):
        sections_text = '\n'.join([
            utils.section_text(s)
            for s in sections
        ])

        return f'New assignment\n' \
               f'<b>{title} | {deadline}</b>\n' \
               f'\n' \
               f'{sections_text}\n'
