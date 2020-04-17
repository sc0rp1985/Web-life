from pymongo import MongoClient
from bs4 import BeautifulSoup
from datetime import datetime
import os




def time_log(func):
    def wrapper(*args, **kwargs):
        dt = datetime.now()
        result = func(*args, **kwargs)
        dt = datetime.now() - dt
        # print("method {name} - {time:d} ms".format(name=func.__name__, time=dt.microseconds()))
        print("method {name}".format(name=func.__name__))
        return result
    return wrapper


class MongoCacheStorage:
    def __init__(self):
        # with open("config.xml") as f:
        #     content = f.read()

        # y = BeautifulSoup(content)
        # cache_db_host = y.connectionstrings.cache.host.contents[0]
        # cache_db_port = y.connectionstrings.cache.port.contents[0]
        # cache_db_name = y.connectionstrings.cache.db_name.contents[0]
        cache_db_host = os.environ.get('MONGO_PORT_27017_TCP_ADDR')
        cache_db_port = os.environ.get('MONGO_PORT_27017_TCP_PORT')
        cache_db_name = os.environ.get('MONGO_DB_NAME')

        self.client = MongoClient(host=cache_db_host, port=int(cache_db_port))
        self.base = self.client[cache_db_name]

    @time_log
    def get_value(self, hash):
        dumps = self.base.dumps
        dump = dumps.find_one({'hash': hash})
        return dump['dump'] if dump is not None else ""

    @time_log
    def put_cache_value(self, hash, dump):
        if self.get_value(hash) == "":
            self.base.dumps.insert({"hash": hash, "dump": dump})
