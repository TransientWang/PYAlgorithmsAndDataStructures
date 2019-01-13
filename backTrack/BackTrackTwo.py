# -*- coding: UTF-8 -*-

def permuteUnique(nums):
    """
    47. 全排列 II
    思路：排序+ DFS + 与前面数字相同剪枝
    与 组合总和2 相似
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums.sort()

    def backTrack(nums):
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sub = backTrack(nums[:i] + nums[i + 1:])
            for j in sub:
                res.append(j + [num])
        return res

    res = backTrack(nums)
    return res


if __name__ == '__main__':
    permuteUnique([1, 1, 3])
