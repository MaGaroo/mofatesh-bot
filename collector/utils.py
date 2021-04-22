import urllib.parse

UNIQUE_URL = 'https://kalampolobazeytoon.com'


def section_text(s):
    result = f'<b>{s[0]}</b>\n{s[1]}\n'
    for text, link in s[2].items():
        result = result.replace(text, f'<a href="{link}">{text}</a>')
    return result


def is_relative_url(url):
    return UNIQUE_URL in urllib.parse.urljoin(UNIQUE_URL, url)


def dirty_url_join(parent, child):
    if is_relative_url(child):
        if 'index.php' in parent:
            return parent.split('index.php')[0] + child
    return urllib.parse.urljoin(parent, child)
