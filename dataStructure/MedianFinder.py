# -*- coding: UTF-8 -*-
from heapq import *


class MedianFinder:

    def __init__(self):
        """
        295.数据流的中位数
        initialize your data structure here.
        """
        self.flag = False
        self.left = []  # 小顶堆
        self.right = []  # 小顶堆

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.flag = not self.flag
        if self.flag:
            heappush(self.right, - heappushpop(self.left, -num))
        else:
            heappush(self.left, -heappushpop(self.right, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if self.flag:
            return self.right[0]

        return (-self.left[0] + self.right[0]) // 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(0)
    obj.addNum(2)
    obj.addNum(4)
    obj.addNum(6)
    param_2 = obj.findMedian()
    print(param_2)
