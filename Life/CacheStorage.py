from Life.MongoCacheStorage import MongoCacheStorage as storage

class CacheStorage:

    def __init__(self):
        self.__storage = storage()

    def get_cache_value(self, hash):
        return self.__storage.get_value(hash)


    def put_cache_value(self, hash, dump):
        self.__storage.put_cache_value(hash, dump)










