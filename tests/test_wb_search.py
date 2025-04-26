# Use if modules can't connect:
# import sys
# import os
# from pathlib import Path

# root_dir = Path(__file__).resolve().parent.parent  
# sys.path.append(str(root_dir))

import pytest
from src.core.sort_type import SortType
from src.core.wb_search import search_by_query

# Test the response difference
def test_sort_type_search():
    popular = search_by_query('синяя куртка', SortType.POPULAR.value).json()
    newly = search_by_query('синяя куртка', SortType.BENEFIT.value).json()

    assert popular != newly

def test_search():
    coat = search_by_query('синяя куртка', SortType.POPULAR.value).json()
    hat = search_by_query('синяя шапка', SortType.POPULAR.value).json()

    assert coat != hat