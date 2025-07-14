class CacheBackend:
    def get(self):
        raise NotImplementedError

    def set(self, data):
        raise NotImplementedError
