from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError('Capacity must be positive!')
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if value is not None:
            self.cache.move_to_end(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if value is not None:
            self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)
