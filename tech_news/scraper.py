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


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
