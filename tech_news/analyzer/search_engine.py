from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)

    search = []

    for item in result:
        search.append((item['title'], item['url']))

    return search


def search_by_date(date):
    try:
        timestamp = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        query = {"timestamp": timestamp}
        result = search_news(query)

        search = []

        for item in result:
            search.append((item['title'], item['url']))

        return search
    except ValueError:
        raise ValueError('Data inválida')


def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    result = search_news(query)

    search = []

    for item in result:
        search.append((item['title'], item['url']))

    return search
