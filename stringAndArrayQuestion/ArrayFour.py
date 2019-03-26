# -*- coding: UTF-8 -*-
import math


def combinationSum3(k, n):
    """
    216. 组合总和 III
    回溯
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    math.sqrt()

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
    220. 存在重复元素 III(review)
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

    #桶排序
    width = t + 1
    if width <= 0:
        return False
    lookup = dict()
    for i in range(len(nums)):
        bucket = nums[i] // width
        if bucket in lookup \
                or (bucket - 1 in lookup and abs(nums[i] - lookup[bucket - 1]) < width)\
                or (bucket + 1 in lookup and abs(nums[i] - lookup[bucket + 1]) < width):
            return True
        lookup[bucket] = nums[i]
        if i >= k:
            lookup.pop(nums[i - k] // width)
    return False

def maximalSquare(matrix):
    """
    221. 最大正方形(review)
    动态规划：dp[x][y] 代表以matrix[x][y]为右下角的正方形的最大面积
    最长边 = min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + 1
    :type matrix: List[List[str]]
    :rtype: int
    """
    # 解法 1
    # if not matrix:
    #     return 0
    # dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    # res = 0
    # for x in range(len(matrix)):
    #     if matrix[x][0] == "1":
    #         res = 1
    #         dp[x][0] = 1
    # for y in range(len(matrix[0])):
    #     if matrix[0][y] == "1":
    #         res = 1
    #         dp[0][y] = 1
    # for x in range(1, len(matrix)):
    #     for y in range(1, len(matrix[0])):
    #         if matrix[x][y] == "1":
    #             # 正方形条件
    #             t = min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + 1
    #             if t > 1:
    #                 dp[x][y] = t
    #                 res = max(dp[x][y], res)
    #             else:
    #                 dp[x][y] = 1
    # return res ** 2
    # 解法 2
    if not matrix:
        return 0
    row = [0] * len(matrix[0])  # 竖着的边的长度
    min_bian = 0
    for i in range(len(matrix)):
        flag = 0  # 在每一行遇到 竖边大于最小正方形边长的时候，flag+=1如果 flag == min_bian + 1则证明遇到了一个更大的正方形
        for j in range(len(matrix[0])):
            row[j] = row[j] + 1 if matrix[i][j] == '1' else 0  # 求每列的中最长竖边
            flag = flag + 1 if row[j] > min_bian else 0  # 求遇到竖边大于 min_bian 的时候，横边有多长
            if flag == min_bian + 1:  # 遇到更大的正放形
                min_bian += 1
                flag = 0
    return min_bian * min_bian


def summaryRanges(nums):
    """
    228. 汇总区间
    :type nums: List[int]
    :rtype: List[str]
    """
    nums.sort()
    p = []
    res = []
    i = 0
    while i < len(nums):
        if not p:
            p.append(nums[i])
            i += 1
        elif nums[i] - p[-1] == 1:
            p.append(nums[i])
            i += 1
        else:
            p = str(p[0]) if len(p) == 1 else str(p[0]) + "->" + str(p[-1])
            res.append(p)
            p = []
    p = str(p[0]) if len(p) == 1 else str(p[0]) + "->" + str(p[-1])
    res.append(p)
    return res


def majorityElement(nums):
    """
    229. 求众数 II
    :type nums: List[int]
    :rtype: List[int]
    """
    # 一、
    # dict1 = dict(Counter(nums))
    # subn = len(nums) // 3
    # return [i for i in dict1 if dict1[i] > subn]
    # 二、
    # h = len(nums) // 3
    # dic = dict()
    # res = []
    # for i in nums:
    #     if dic.get(i, "#") == "#":
    #         dic[i] = 1
    #     else:
    #         dic[i] += 1
    # for k, v in dic.items():
    #     if v > h:
    #         res.append(k)
    # return res
    # 三、
    # 摩尔投票升级,有超过 1/3 的元素结果数量一定小于等于两个
    # 先选出两个候选人A, B, 遍历数组，如果投A（等于A），则A的票数加1;
    # 如果投B，B的票数加1；
    # 如果A, B都不投（即与A，B都不相等）, 那么检查此时是否AB中候选人的票数是否为0，如果为0, 则成为新的候选人；
    # 如果A, B两个人的票数都不为0，那么A, B两个候选人的票数均减1；
    # 遍历结束后选出两个候选人，但是这两个候选人是否满足 > n / 3，还需要再遍历一遍数组，找出两个候选人的具体票数
    num1 = num2 = 1000000  # 可以设置为任意值，如果设置为nums[0] 还需要判断 len(nums) >0,
    cnt1 = cnt2 = 0
    for num in nums:
        if num == num1:
            cnt1 += 1
        elif num == num2:
            cnt2 += 1
        elif cnt1 == 0:
            num1 = num
            cnt1 += 1
        elif cnt2 == 0:
            num2 = num
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    # 找出个数
    cnt1 = nums.count(num1)
    cnt2 = nums.count(num2)
    res = []
    if cnt1 > int(len(nums) / 3):
        res.append(num1)
    if cnt2 > int(len(nums) / 3):
        res.append(num2)
    return res


def countDigitOne(n):
    """
    233. 数字1的个数
    https://www.cnblogs.com/grandyang/p/4629032.html
    :type n: int
    :rtype: int
    """
    # length = len(str(n))  # w位数
    # time = 0
    # base = 1
    # for i in range(length):
    #     if i == 0:  # 10 位数与个位数的1的总和
    #         r = n // (base * 10)
    #         current = n % (base * 10)
    #         time += r * base
    #         if current >= 1:
    #             time += 1
    #     else:  # 其他位数
    #         r = n // (base * 10)
    #         current = (n % (base * 10)) // base
    #         end = n % base
    #         if current == 0:
    #             time += r * base
    #         elif current == 1:
    #             time += r * base + end + 1
    #         else:
    #             time += (r + 1) * base
    #     base = base * 10
    # return time
    # 解法二
    ones, m = 0, 1
    while m <= n:
        ones += (n // m + 8) // 10 * m
        ones += (n // m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones


if __name__ == '__main__':

    print(countDigitOne(1001))
