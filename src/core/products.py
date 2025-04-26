import requests
from .sort_type import SortType
from .wb_search import search_by_id, search_by_query

class Products:

    def __init__(self, query: str, sort: SortType = 'popular'):
        self.__products = search_by_query(query, sort).json()['data']['products']
    
    def yiled_id(self):
        for product in self.__products: 
            yield product['id']