from cachetools import TTLCache
from config import CACHE_TTL
from .base import CacheBackend

class InMemoryCache(CacheBackend):
    def __init__(self):
        self.cache = TTLCache(maxsize=1, ttl=CACHE_TTL)

    def get(self):
        return self.cache.get("synonyms")

    def set(self, data):
        self.cache["synonyms"] = data
