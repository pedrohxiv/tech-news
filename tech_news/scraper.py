import requests
import time
from parsel import Selector


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None
    finally:
        time.sleep(1)


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css('.entry-title a::attr(href)').getall()


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.next::attr(href)').get()


def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css('link[rel=canonical]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get().strip()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('li.meta-author span.author a::text').get()
    reading_time = int(selector.css(
        'li.meta-reading-time::text').get().split()[0])
    summary = "".join(selector.css(
        'div.entry-content > p:first-of-type *::text').getall()).strip()
    category = selector.css('span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
