from core.parser.get_basket_id import get_basket_id
from core.parser.image import save_image
import requests
from .sort_type import SortType
from .wb_search import search_by_id, search_by_query
from .product import Product

class Products:
    
    """
    Products parsed from query.

    Properties:
    products_data (dict): returns dict with products data
    """

    def __init__(self, query: str, show_high_rated_only: bool, sort: SortType = 'popular'):
        self.__data = search_by_query(query, sort, show_high_rated_only).json()['data']['products']
    
    @property
    def products_data(self):
        return self.__data

    @property
    def lenght(self):
        return len(self.__data)

    def __iter__(self):
        return iter(Product(self.__data))

    def __getitem__(self, index):
        return Product(self.__data[index])  