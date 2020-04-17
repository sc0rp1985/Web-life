import random
import hashlib
from Life.CacheStorage import *



class LifeWorld:

    DUMP_DELIMITER = '|'
    __storage = CacheStorage()
    @staticmethod
    def __test_init():
        __world = LifeWorld.__get_empty_world(10);
        #             0  1  2  3  4  5  6  7  8  9
        __world[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        __world[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        __world[8] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
        __world[9] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        return __world

    @staticmethod
    def __test_random_init(size):
        result = LifeWorld.__get_empty_world(size)
        for row in range(size):
            for col in range(size):
                result[row][col] = random.randint(0, 1)
        return result

    @staticmethod
    def __get_neighbor_count(world, col, row):
        count = 0
        size = len(world)
        for i in range(row - 1, row + 2):
            row_index = i if 0 <= i < size else abs(abs(i) - size)
            for j in range(col - 1, col + 2):
                col_index = j if 0 <= j < size else abs(abs(j) - size)

                if row_index != row or col_index != col:
                    if world[row_index][col_index] == 1:
                        count += 1
        return count

    @staticmethod
    def __get_empty_world(size):
        a = [[0] * size for i in range(size)]
        return a

    @staticmethod
    def get_init_world(size, is_random):
        return LifeWorld.__test_random_init(size) if is_random else LifeWorld.__test_init()

    @staticmethod
    def next_generation(size, hash_, is_random):
        if hash_ == "":
            world = LifeWorld.get_init_world(size, is_random)
            LifeWorld.__put_dump_to_cache(world)
            return world
        else:
            dump = LifeWorld.__get_dump_by_hash(hash_)
            world = LifeWorld.__get_world_from_dump(dump)

        tmp = LifeWorld.__get_empty_world(size)
        for row in range(len(tmp)):
            for col in range(len(tmp)):
                count = LifeWorld.__get_neighbor_count(world, col, row)
                if count > 3 or count < 2:
                    tmp[row][col] = 0
                elif count == 2:
                    tmp[row][col] = world[row][col]
                elif count == 3:
                    tmp[row][col] = 1
        new_hash = LifeWorld.__put_dump_to_cache(tmp)
        return {new_hash: tmp}

    @staticmethod
    def __get_dump_by_hash(hash):
        cache_dump = LifeWorld.__storage.get_cache_value(hash) if hash != "" else ""
        return cache_dump if cache_dump is not None else ""

    @staticmethod
    def __put_dump_to_cache(world):
        new_dump = LifeWorld.get_dump_from_world(world)
        hash = LifeWorld.get_hash(new_dump)
        LifeWorld.__storage.put_cache_value(hash, new_dump)
        return hash

    #@staticmethod
    #def get_world(self):
    #    return self.__world

    #def get_generation(self):
    #    return self.__generation

    #def get_empty(self):
    #    return self.__empty

    @staticmethod
    def get_hash(dump):
        _hash = hashlib.md5(dump.encode('utf-8')).hexdigest()
        return _hash

    @staticmethod
    def get_dump_from_world(world):
        _str = LifeWorld.DUMP_DELIMITER.join(map(lambda x: ''.join(map(str, x)), world))
        return _str

    @staticmethod
    def __get_world_from_dump(dump):
        rows = dump.split(LifeWorld.DUMP_DELIMITER)
        return list(map(lambda x: list(map(int, x)), rows))
