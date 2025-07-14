from config import USE_REDIS_CACHE
from .redis_cache import RedisCache
from .memory_cache import InMemoryCache

cache = RedisCache() if USE_REDIS_CACHE else InMemoryCache()
