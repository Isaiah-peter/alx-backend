#!/usr/bin/python3
"""Basic cache"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        if key != None and self.cache_data.get(key) != None:
            return self.cache_data.get(key)
        else:
            return None
