from core.parser.product import Product
from core.parser.products import Products
from core.parser.sort_type import SortType


def wb_parse(query: str, sort_type: SortType = SortType.POPULAR.value, product_amount: int = 3):
    
    """
    Return wildberries products data from query printing process.

    Args:
    query (string): search query.
    sort_type (SortType): sort type (SortType.POPULAR.value is by default).
    product_amount (int): output amount of products.
    
    Returns:
    dict: product data dictionaries
    
    Example:
    >>> wb_parse("blue jeans", SortType.Rate.value, 5)
    {0: {_Product__brand: brand_name, ...}, 
    1: {...}, 
    4: {...}
    }
    """

    products = Products(query, sort_type)
    products_data = {}

    for i in range(product_amount):
        product = Product(products, i)
        current_attributes = product.__dict__
        for ignored_attribute in product.ignored_attributes:
            del current_attributes[ignored_attribute] # delete attributes that we don't want user to see
        products_data[i] = current_attributes
        print(product)

    return products_data