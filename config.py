import os
from dotenv import load_dotenv

load_dotenv()

USE_REDIS_CACHE = os.getenv("USE_REDIS_CACHE", "False") == "True"
CACHE_TTL = int(os.getenv("CACHE_TTL", 300))
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
