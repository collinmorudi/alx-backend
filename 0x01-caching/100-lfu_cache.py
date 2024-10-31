#!/usr/bin/python3
"""
LFU Caching Module

This module defines the LFUCache class, inheriting from BaseCaching.
It implements a Least Frequently Used (LFU) caching system where, when
the cache reaches its limit, the item with the lowest access frequency
is discarded. If multiple items have the same frequency, the Least
Recently Used (LRU) item is discarded.
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that uses a Least Frequently Used (LFU) caching system.

    Inherits from BaseCaching and overrides the put and get methods to
    add caching behavior where the least frequently accessed item is
    discarded when the cache reaches the limit.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance with tracking for frequencies
        and recency of cache items.
        """
        super().__init__()
        self.usage_freq = {}
        self.recent_usage = {}

    def put(self, key, item):
        """
        Add an item to the cache with LFU behavior.

        If the number of items exceeds the maximum allowed in BaseCaching,
        it discards the item with the lowest frequency of access. In case
        of ties, it discards the Least Recently Used (LRU) item. If key
        or item is None, it performs no action.

        Args:
            key (str): The key for the item to store in the cache.
            item (Any): The value associated with the key to be cached.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the LFU key, tie-breaking with LRU
            lfu_key = min(self.usage_freq, key=lambda k: (
                self.usage_freq[k], self.recent_usage[k]
            ))
            del self.cache_data[lfu_key]
            del self.usage_freq[lfu_key]
            del self.recent_usage[lfu_key]
            print("DISCARD:", lfu_key)

        # Update or add the item
        self.cache_data[key] = item
        self.usage_freq[key] = self.usage_freq.get(key, 0) + 1
        self.recent_usage[key] = self._current_time()

    def get(self, key):
        """
        Retrieve an item from the cache and update its usage frequency.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            Any: The cached value linked to the key, or None if the key is
            None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update usage frequency and recency
        self.usage_freq[key] += 1
        self.recent_usage[key] = self._current_time()
        return self.cache_data[key]

    def _current_time(self):
        """
        Private helper method to get the current usage timestamp.

        Returns:
            int: An incrementing count representing the usage order.
        """
        return len(self.recent_usage)
