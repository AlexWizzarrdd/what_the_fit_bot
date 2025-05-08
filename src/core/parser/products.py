from core.parser.get_basket_id import get_basket_id
from core.parser.image import save_image
import requests
from .sort_type import SortType
from .wb_search import search_by_id, search_by_query

class Products:
    
    """
    Products which is parsed from query.

    Properties:
    products_data (dict): returns dict with products data

    Methods:
    get_id(product_index) -> int: returns product id
    """

    def __init__(self, query: str, sort: SortType = 'popular'):
        self.__products_data = search_by_query(query, sort).json()['data']['products']
    
    @property
    def products_data(self):
        return self.__products_data

    # For future development:
    # def yiled_id(products):
    #     for product in self.__products: 
    #         yield product['id']

    def get_id(self, product_index: int):
        return self.__products_data[product_index]['id']