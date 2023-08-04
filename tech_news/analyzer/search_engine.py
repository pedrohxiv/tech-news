from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)

    search = []

    for item in result:
        search.append((item['title'], item['url']))

    return search


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
