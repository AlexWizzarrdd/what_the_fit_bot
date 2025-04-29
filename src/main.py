from core.sort_type import SortType
from core.wb_search import search_by_id, search_by_query
from core.products import Products
from core.product import Product
from core.image import scrap_image, convert_to_png
import requests

products = Products('синяя куртка', SortType.POPULAR.value)

for product_id in products.yiled_id():
    product = Product(product_id)
    print(product)