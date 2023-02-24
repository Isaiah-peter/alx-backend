#!/usr/bin/python3
"""Basic cache"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache"""

    def put(self, key, item):
        """put(key, item) -> None"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get(key) -> None"""
        if key is not None and self.cache_data.get(key) is not None:
            return self.cache_data.get(key)
        else:
            return None
