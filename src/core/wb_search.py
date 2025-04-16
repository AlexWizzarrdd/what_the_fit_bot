import requests

def search(query: str):
    
    payload = {
    'ab_vector_qi_from': 'extend_cos',
    'appType': '1',
    'curr': 'rub',
    'dest': '-5818883',
    'hide_dtype': '13',
    'lang': 'ru',
    'page': '1',
    'query': query,
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '1',
    'suppressSpellcheck': 'false',
    }

    return requests.get('https://search.wb.ru/exactmatch/ru/common/v9/search', params=payload)



