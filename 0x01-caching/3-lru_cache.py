#!/usr/bin/python3
"""
LRU Caching Module

This module defines the LRUCache class, inheriting from BaseCaching.
It implements a Least Recently Used (LRU) caching system where, when
the cache reaches its limit, the least recently used item is discarded.
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that uses a Least Recently Used (LRU) caching system.

    Inherits from BaseCaching and overrides the put and get methods to
    add caching behavior where the least recently accessed item is
    discarded when the cache reaches the limit.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance with tracking for item recency.
        """
        super().__init__()
        self.recency = []

    def put(self, key, item):
        """
        Add an item to the cache with LRU behavior.

        If the number of items exceeds the maximum allowed in BaseCaching,
        it discards the least recently used item. If key or item is None,
        it performs no action.

        Args:
            key (str): The key for the item to store in the cache.
            item (Any): The value associated with the key to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.recency.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = self.recency.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add/update the item and refresh recency
        self.cache_data[key] = item
        self.recency.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache and update its recency.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            Any: The cached value linked to the key, or None if the key is
            None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update recency
        self.recency.remove(key)
        self.recency.append(key)
        return self.cache_data[key]
