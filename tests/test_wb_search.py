# Use if modules can't connect:
# import sys
# import os
# from pathlib import Path

# root_dir = Path(__file__).resolve().parent.parent  
# sys.path.append(str(root_dir))

import pytest
from src.core.sort_type import SortType
from src.core.wb_search import search

# Test the response difference
def test_sort_type_search():
    popular = search('синяя куртка', SortType.POPULAR.value).json()
    newly = search('синяя куртка', SortType.BENEFIT.value).json()

    assert popular != newly

def test_search():
    coat = search('синяя куртка', SortType.POPULAR.value).json()
    hat = search('синяя шапка', SortType.POPULAR.value).json()

    assert coat != hat