#!/usr/bin/python3
"""
LIFO Caching Module

This module defines the LIFOCache class that inherits from BaseCaching.
It implements a last-in, first-out caching strategy where the most recently
added item is discarded once the cache reaches its maximum limit.
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that uses a Last-In-First-Out (LIFO) caching system.

    Inherits from BaseCaching and overrides the put and get methods to
    add caching behavior where the last inserted item is the first to
    be discarded when the cache reaches the limit.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance by calling the parent class's
        __init__ method to initialize the cache_data dictionary.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache with LIFO behavior.

        If the number of items exceeds the maximum allowed in BaseCaching,
        it discards the most recent item. If key or item is None, it performs
        no action.

        Args:
            key (str): The key for the item to store in the cache.
            item (Any): The value associated with the key to be cached.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None and self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            Any: The cached value linked to the key, or None if the key is
            None or doesn't exist in the cache.
        """
        return self.cache_data.get(key, None)
