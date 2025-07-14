import redis
import json
from config import CACHE_TTL, REDIS_HOST, REDIS_PORT
from .base import CacheBackend

class RedisCache(CacheBackend):
    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get(self):
        data = self.client.get("synonyms")
        return json.loads(data) if data else None

    def set(self, data):
        self.client.setex("synonyms", CACHE_TTL, json.dumps([d.dict() for d in data]))
