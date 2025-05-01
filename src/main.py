from core.sort_type import SortType
from core.wb_parse import parse_products_data
from core.wb_search import search_by_id, search_by_query
from core.products import Products
from core.product import Product
from core.image import scrap_image, convert_to_png
import requests

products_data = parse_products_data('красная шляпа')