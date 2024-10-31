#!/usr/bin/python3
"""
FIFO Caching Module

This module defines the FIFOCache class that inherits from BaseCaching.
It implements a first-in, first-out caching strategy where the oldest
added items are discarded once the cache reaches its maximum limit.
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that uses a First-In-First-Out (FIFO) caching system.

    Inherits from BaseCaching and overrides the put and get methods to
    add caching behavior where the first inserted item is the first to
    be discarded when the cache reaches the limit.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance by calling the parent class's
        __init__ method to initialize the cache_data dictionary.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache with FIFO behavior.

        If the number of items exceeds the maximum allowed in BaseCaching,
        it discards the oldest item. If key or item is None, it performs
        no action.

        Args:
            key (str): The key for the item to store in the cache.
            item (Any): The value associated with the key to be cached.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
            self.order.append(key)

        self.cache_data[key] = item

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
