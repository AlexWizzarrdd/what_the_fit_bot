import requests
from .sort_type import SortType
from .wb_search import search_by_id, search_by_query

class Product:

    def __init__(self, product_id: int):
        self.__data = search_by_id(product_id).json()['data']['products'][0]
        self.__link = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
        self.__brand = self.__data['brand']
        self.__name = self.__data['name']
        self.__price = self.parse_price() 
        self.__review_rating = self.__data['reviewRating']
        self.__supplier_rating = self.__data['supplierRating']

    @property
    def data(self):
        return self.__data

    @property
    def link(self):
        return self.__link

    @property
    def brand(self):
        return self.__brand

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def review_rating(self):
        return self.__review_rating

    @property
    def supplier_rating(self):
        return self.__supplier_rating

    # make examples printable
    def __str__(self):
        attributes = ''
        for attribute, value in vars(self).items():
            if not attribute.startswith('_Product__data'): 
                attributes += f"{attribute}: {value}\n"
        return attributes

    # look for price info 
    # stepping into every product size 
    # while finally get It
    def parse_price(self):
        for i in range(len(self.__data['sizes']) - 1): 
            try:
                price = self.__data['sizes'][i]['price']['product'] // 100
                return f"{price:,}" # return readable price
            except :
                continue


