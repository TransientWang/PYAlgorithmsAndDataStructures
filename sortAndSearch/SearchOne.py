# -*- coding: UTF-8 -*-
def searchInsert(nums, target):
    """
    35. 搜索插入位置
    思路：二分搜索
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # for i in range(len(nums)):
    #     if target == nums[i]:
    #         return i
    #     elif target < nums[i]:
    #         return i
    # return len(nums)

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left