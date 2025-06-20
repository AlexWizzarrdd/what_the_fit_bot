from core.parser.criteria import Criteria
from core.parser.product import Product
from core.parser.products import Products
from core.parser.sort_type import SortType

def wb_parse(
    query: str,
    sort_type: SortType = SortType.POPULAR.value, 
    product_amount: int = 3, 
    show_high_rated_only: bool = True,
    *criteria: Criteria
    ):
    
    """
    Return wildberries products data from query printing process.

    Args:
    query (string): search a query.
    *criteria (Criteria): predicates that gets a Product variable as an arguement
    sort_type (SortType): sort type (SortType.POPULAR.value is by default).
    product_amount (int): output amount of products.
    show_high_rated_only (bool): if True show high rated products only
    
    Returns:
    dict: product data dictionaries
    
    Example:
    >>> wb_parse("blue jeans", has_feedbacks, SortType.Rate.value, 5, False)
    {0: {_Product__brand: brand_name, ...}, 
    1: {...}, 
    4: {...}
    }
    """

    products = Products(query, show_high_rated_only, sort_type)
    result = {}
    product_count = product_amount
    
    for i in range(products.lenght):
        if products.lenght == 0:
            raise ValueError("No product is found")

        if product_count == 0:
            return result
        product = products[i]

        for criterion in criteria:
            if not criterion(product):
                continue

        current_attributes = __delete_attributes(
            product.__dict__, 
            product.ignored_attributes
            ) 

        result[i] = current_attributes
        print(product)
        product_count -= 1

def __delete_attributes(attributes: dict, ignored_attributes):
    for ignored_attribute in ignored_attributes:
            # delete attributes that we don't want user to see
            del attributes[ignored_attribute]
    return attributes        
    