# -*- coding: UTF-8 -*-
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
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
        if self.hash.get(key) is None:
            if self.cur == 0:
                self.hash.pop(self.list.pop())
                self.list.insert(0, key)
            else:
                self.cur -= 1
                self.list.insert(0, key)
        else:
            self.list.remove(key)
            self.list.insert(0, key)
        self.hash[key] = value





if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.put(4,1)
    print(cache.get(1))
    print(cache.get(2))
