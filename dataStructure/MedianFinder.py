# -*- coding: UTF-8 -*-
from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        295. 数据流的中位数(reveiw)
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.tag = True

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.tag:
            heappush(self.left, - heappushpop(self.right, float(num)))
        else:
            heappush(self.right, - heappushpop(self.left, -float(num)))

        self.tag = not self.tag

    def findMedian(self):
        """
        :rtype: float
        """
        return -self.left[0] if not self.tag else (self.right[0] - self.left[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(0)
    obj.addNum(2)
    obj.addNum(4)
    obj.addNum(6)
    param_2 = obj.findMedian()
    print(param_2)
