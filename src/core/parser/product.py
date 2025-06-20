import requests
from .sort_type import SortType
from .wb_search import search_by_id, search_by_query
from core.parser.get_basket_id import get_basket_id
from core.parser.image import convert_to_png, save_image, scrap_image

class Product:

    """
    Product which is parsed from products data.

    Attributes:
    ignored_attributes (tuple): attributes that we don't want to print. 
    """

    ignored_attributes = ('_Product__data',
                          '_Product__id',
                          '_Product__basket_id'
                         )

    def __init__(self, product_data: dict):
        if not product_data:
            raise ValueError("Empty dictionary was passed on")
        self.__data = product_data
        self.__id = self.__data['id']
        self.__link = f"https://www.wildberries.ru/catalog/{self.__id}/detail.aspx"
        self.__brand = self.__data['brand']
        self.__name = self.__data['name']
        self.__price = self.__parse_price() 
        self.__review_rating = self.__data['reviewRating']
        self.__supplier_rating = self.__data['supplierRating']
        self.__basket_id = get_basket_id(self.__id)
        self.__image_link = ( 
            f"https://basket-{self.__basket_id}.wbbasket.ru/vol{self.__id // 10**5}/"
            f"part{self.__id // 10**3}/{self.__id}/images/big/1.webp" 
        )
        self.__image_path = save_image(self.__image_link, self.__id, self.__basket_id)

    @property
    def product_data(self):
        return self.__data

    @property
    def id(self):
        return self.__id

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

    @property
    def image_link(self):
        return self.__image_link

    @property
    def image_path(self):
        return self.__image_path

    def __str__(self):
        attributes = ''
        for attribute, value in vars(self).items():
            if not attribute.startswith(self.ignored_attributes): 
                attributes += f"{attribute}: {value}\n"
        return attributes

    def __parse_price(self):
        """
        look for price info stepping into every product size 
        while finally get It
        """

        price = self.__data['sizes'][0]['price']['product'] // 100
        if not isinstance(price, (int, float)):
            raise TypeError("Had tried to parse price but It wasn't number")
        return f"{price:,}" # return readable price


