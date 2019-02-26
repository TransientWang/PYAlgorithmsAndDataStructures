# -*- coding: UTF-8 -*-
class RandomizedSet:

    def __init__(self):
        """
        380. 常数时间插入、删除和获取随机元素(review)
        Initialize your data structure here.
        """
        self.r = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.r:
            return False
        else:
            self.r.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.r:
            r.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        ind = random.randint(0,len(self.r)-1)
        return list(self.r)[ind]


if __name__ == '__main__':
    r = RandomizedSet()
    print(r.insert(1))
    print(r.r)
    print(r.remove(1))
    print(r.getRandom())
