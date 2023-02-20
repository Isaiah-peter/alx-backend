#!/usr/bin/env python3
"""method named get_page that takes
two integer arguments page with
default value 1 and page_size with default value 10."""


import csv
import math
from typing import List, Dict


def index_range(size, page_size):
    """index range"""
    total = size * page_size
    if (total == page_size):
        return tuple([0, page_size])

    return tuple([total - page_size, total])


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns list according to the given page"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        res = index_range(page, page_size)
        result = self.dataset()
        return result[res[0]:res[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return dictionary"""
        result = self.get_page(page, page_size)
        dataset = self.dataset()
        prev = None
        nexts = page + 1
        total_pages = int(len(dataset) / page_size)

        if(page_size > 1):
            prev = page - 1

        if(total_pages < nexts):
            nexts = None

        return {
            "page_size": page_size,
            "page": page,
            "data": result,
            "next_page": nexts,
            "prev_page": prev,
            "total_pages": total_pages
        }
