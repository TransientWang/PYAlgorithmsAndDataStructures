# -*- coding: UTF-8 -*-
class LRUCache:

    def __init__(self, capacity):
        """
        146.LRU缓存机制(review)
        acity: int
        """
        self.hash = {}
        self.cur = capacity
        self.list = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.list:
            self.list.remove(key)
            self.list.insert(0, key)
            return self.hash.get(key)
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.hash.get(key):
            self.list.remove(key)
            self.list.insert(0, key)
        elif self.cur == 0:  # cur减少到0的时候就开始往外弹过期的
            self.hash.pop(self.list.pop())
            self.list.insert(0, key)
        else:
            self.cur -= 1  # cur不为0就减1
            self.list.insert(0, key)

        self.hash[key] = value


if __name__ == '__main__':
    cache = LRUCache(1)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
