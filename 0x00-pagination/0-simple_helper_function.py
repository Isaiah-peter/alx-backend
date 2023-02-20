#!/usr/bin/env python3
"""function named index_range that
takes two integer arguments page and page_size"""


def index_range(size, page_size):
    """index range"""
    total = size * page_size
    if (total == page_size):
        return tuple([0, page_size])

    return tuple([total - page_size, total])
