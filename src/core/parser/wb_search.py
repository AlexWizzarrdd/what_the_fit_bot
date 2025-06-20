import requests
from .sort_type import SortType

def search_by_query(query: str, sort_type: SortType, show_high_rated_only: bool):
    
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
    'sort': sort_type,
    'spp': '1',
    'suppressSpellcheck': 'false',
    }

    if show_high_rated_only:
        payload["frating"] = "1"

    result = requests.get(
        'https://search.wb.ru/exactmatch/ru/common/v9/search', 
        params=payload
        )

    if not result.status_code == 200:
        raise requests.exceptions.ConnectionError()
    return result

def search_by_id(product_id: int):
    
    return requests.get(
        f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1255987&hide_dtype=13&spp=30&ab_testing=false&lang=ru&nm={product_id}")
