# -*- coding: UTF-8 -*-
# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return len(self.nums) > 0

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        t = self.nums.pop(0)
        return t


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        284. 顶端迭代器
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.t = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.t:
            self.t = self.iterator.next()
            return self.t
        else:
            return self.t

    def next(self):
        """
        :rtype: int
        """
        if self.t:
            p = self.t
            self.t = None
            return p
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() == True or self.t != None


if __name__ == '__main__':
    pee = PeekingIterator(Iterator([1, 2, 3, 4]))
    print(pee.hasNext())
    print(pee.peek())
    print(pee.peek())
    print(pee.next())
    print(pee.next())
    print(pee.peek())
    print(pee.peek())
    print(pee.next())
    print(pee.hasNext())
    print(pee.peek())
    print(pee.hasNext())
    print(pee.next())
    print(pee.hasNext())
