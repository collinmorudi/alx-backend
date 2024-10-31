#!/usr/bin/env python3
""" BasicCache module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without limits.
    """
    def put(self, key, item):
        """ Add an item to the cache.

        Args:
            key (str): The key to store the item under.
            item (any): The item to store.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key.

        Args:
            key (str): The key to retrieve the item for.

        Returns:
            any: The item associated with the key, or None if the key is
            None or does not exist.
        """
        return self.cache_data.get(key, None)
