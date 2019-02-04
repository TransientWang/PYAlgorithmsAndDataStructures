# -*- coding: UTF-8 -*-
def combinationSum3(k, n):
    """
    216. 组合总和 III
    回溯
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []

    def find(s_list, begin, end):
        if len(s_list) == k:
            if sum(s_list) == n:
                res.append(s_list)
            return
        for i in range(begin, end):
            find(s_list + [i], i + 1, end)

    find([], 1, min(n, 10))
    return res


def containsNearbyAlmostDuplicate(nums, k, t):
    """
    220. 存在重复元素 III
    滑动窗口
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    # n = len(nums)
    # if t == 0 and n == len(set(nums)):
    #     return False
    #
    # for i in range(len(nums)):
    #     j = i + 1
    #     while j < len(nums) and j - i <= k:
    #         t1 = nums[i]
    #         t2 = nums[j]
    #         if abs(t1 - t2) <= t:
    #             return True
    #         j += 1
    # return False
    lenth = len(nums)
    a = set()  # set集合，是一个无序且不重复的元素集合。
    for i in range(lenth):
        if t == 0:
            if nums[i] in a:
                return True
        else:
            for atem in a:
                if abs(nums[i] - atem) <= t:
                    return True
        a.add(nums[i])
        if len(a) == k + 1:
            a.remove(nums[i - k])
    return False


if __name__ == '__main__':
    print(containsNearbyAlmostDuplicate([7, 2, 8],
                                        2,
                                        1))
