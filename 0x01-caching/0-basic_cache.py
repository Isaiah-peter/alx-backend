#!/usr/bin/python3
"""Basic cache"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache"""

    def put(self, key, item):
        """put(key, item) -> None"""
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """get(key) -> None"""
        if key != None and self.cache_data.get(key) != None:
            return self.cache_data.get(key)
        else:
            return None
