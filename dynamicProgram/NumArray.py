# -*- coding: UTF-8 -*-
class NumArray(object):
    '''
    求数组切片
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.arr=[None for i in range(len(nums)+1)]
        self.arr[0] =0
        for j in range(len(nums)):
            self.arr[j+1]=self.arr[j]+nums[j]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j] - self.arr[i]