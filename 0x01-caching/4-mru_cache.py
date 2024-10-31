#!/usr/bin/python3
"""
MRU Caching Module

This module defines the MRUCache class, inheriting from BaseCaching.
It implements a Most Recently Used (MRU) caching system where, when
the cache reaches its limit, the most recently used item is discarded.
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that uses a Most Recently Used (MRU) caching system.

    Inherits from BaseCaching and overrides the put and get methods to
    add caching behavior where the most recently accessed item is
    discarded when the cache reaches the limit.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance with tracking for most recent item.
        """
        super().__init__()
        self.recently_used = None

    def put(self, key, item):
        """
        Add an item to the cache with MRU behavior.

        If the number of items exceeds the maximum allowed in BaseCaching,
        it discards the most recently used item. If key or item is None,
        it performs no action.

        Args:
            key (str): The key for the item to store in the cache.
            item (Any): The value associated with the key to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.recently_used:
                    # Discard the most recently used item
                    print("DISCARD:", self.recently_used)
                    del self.cache_data[self.recently_used]

            # Add the new item to the cache
            self.cache_data[key] = item
        # Update the most recently used key
        self.recently_used = key

    def get(self, key):
        """
        Retrieve an item from the cache and update its MRU status.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            Any: The cached value linked to the key, or None if the key is
            None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the most recently used key
        self.recently_used = key
        return self.cache_data[key]
