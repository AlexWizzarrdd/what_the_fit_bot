from core.sort_type import SortType
from core.wb_search import search
import requests

response = search('синяя куртка', SortType.RATE)
json_dict = response.json()
print(response.status_code)
print(json_dict)
