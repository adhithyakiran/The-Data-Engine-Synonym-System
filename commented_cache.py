from cachetools import TTLCache

cache = TTLCache(maxsize=1, ttl=300)

def get_cached_synonyms():
    return cache.get("synonyms")

def set_cached_synonyms(data):
    cache["synonyms"] = data
