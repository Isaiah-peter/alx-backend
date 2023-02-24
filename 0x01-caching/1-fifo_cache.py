#!/usr/bin/python3
"""FIFOCache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache"""

    def __init__(self):
        """initial"""
        super().__init__()

    def put(self, key, item):
        """add to the cache"""
        if (key != None and item != None):
            self.cache_data[key] = item
            if (len(self.cache_data) > self.MAX_ITEMS):
                first_key = list(self.cache_data.keys())[0]
                del(self.cache_data[first_key])
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """get the item"""
        if (key != None and self.cache_data[key] != None):
            return self.cache_data[key]
        else:
            return None
