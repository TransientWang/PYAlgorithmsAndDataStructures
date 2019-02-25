# -*- coding: UTF-8 -*-
import collections
from copy import deepcopy


def threeSum(nums):
    '''
    15.三数之和（review）
    先排顺序，然后双指针遍历,
    :param nums:
    :return:
    '''
    nums.sort()
    res = []
    for i, v in enumerate(nums):
        if v > 0: break
        if i > 0 and nums[i] == nums[i - 1]: continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            tmp = nums[left] + nums[right] + v
            if tmp == 0:
                res.append([v, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif tmp < 0:
                left += 1
            elif tmp > 0:
                right -= 1
    return res


def threeSumClosest(nums, target):
    '''
    16.最接近的三数之和
    与三数值和思路差不多
    但是要注意的是tmp需要与target比较
    :param nums:
    :param target:
    :return:
    '''
    res = 10000
    nums.sort()
    r = 0
    for i in range(len(nums)-2):
        tmp = nums[i]
        left = i+1
        right = len(nums) - 1
        while left < right:
            num = tmp + nums[left] + nums[right]
            if abs(target - num) < res:
                res = abs(target - num)
                r = num
            if num == target:
                return target
            elif num > target:
                right -= 1
            else:
                left += 1
    return r


def setZeroes(matrix):
    '''
    73.矩阵置零
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
    思路：首先想到的是行里发现有0 的话那么，这一行肯定是首先需要全都变为 0 的
    然后 列变为0 但是在继续判断是会因为  之前这行的某一个 数字因为其他行的影响为0，而误删掉这一整行
    所以可以 用一个辅助数组，来记录那一列需要删除，而不要着急 遇到0就删除一整行在这一行每个索引遍历完后再
    删除这一行，最后遍历辅助数组 删除相应的列就好
    如果不用辅助数组 可以用 矩阵第一行来记录
    '''
    # 解法
    m = len(matrix)
    n = len(matrix[0])
    idx = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                idx.append((i, j))

    # while idx:
    #     i, j = idx.pop()
    #     matrix[i] = [0] * n
    #     for k in matrix:
    #         k[j] = 0
    # 解法
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 0:
    #             matrix[i][j] = 2 ** 31
    #             for y in range(len(matrix[0])):
    #                 if matrix[i][y] != 0:
    #                     matrix[i][y] = 2 ** 31
    #             for x in range(len(matrix)):
    #                 if matrix[x][j] != 0:
    #                     matrix[x][j] = 2 ** 31
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 2 ** 31:
    #             matrix[i][j] = 0
    # return matrix


def groupAnagrams(strs):
    if len(strs) is 0:
        return []
    dp = [[strs[0]]]

    for i in range(1, len(strs)):
        # l = list(strs[i])
        l = sorted(strs[i])
        flag = False
        for j in range(len(dp)):
            r = sorted(dp[j][0])
            if l == r:
                flag = False
                dp[j].append(strs[i])
                break
            else:
                flag = True

        if flag:
            dp.append([strs[i]])
    return dp


'''
字谜分组
维护一个映射 ans : {String -> List}，其中每个键
ext{K}K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 ext{K}K。
在 Java 中，我们将键存储为字符串，例如，code。 在 Python 中，我们将键存储为散列化元组，
例如，('c', 'o', 'd', 'e')。
'''


def groupAnagramsOne(strs):
    ans = collections.defaultdict(list)

    for i in strs:
        ans[str(sorted(i))].append(i)

    r = []
    for i in ans.values():
        r.append(i)
    return r


def lengthOfLongestSubstring(s):
    '''
    3.无重复字符的最长子串
    维持一个滑动窗口
    有三种情况需要考虑
    一、当新加入的字符 不存在之前的子序列中的时候那么这个在字符就可以加入子串中
    二、当新加入的字符已经存在于子串中的时候，而且重复的位置在子串的第一位的时候，可以删除第一位的字符，并在结尾加入当前字符
    三、当新加入的字符已经存在于子串中的时候，而且重复的位置不在子串的第一位的时候，需要删除重复位置之前的子串
    并新加入当前字符
    最后需要有一个 值记录滑动窗口的最大值
    '''
    window = []
    max_len = 0
    for i, o in enumerate(s):
        if o not in window:
            window.append(o)
        elif o == window[0]:
            window.append(o)
            window.pop(0)
        else:
            max_len = max(len(window), max_len)
            window = window[window.index(o) + 1:]
            window.append(o)

    max_len = max(len(window), max_len)
    return max_len


def longestPalindrome(s):
    '''
    5.最长回文子串
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000
    Manacher's
    https://www.cnblogs.com/mini-coconut/p/9074315.html
    '''
    r = ["#"]
    for i in s:
        r.append(i)
        r.append("#")
    lens = [1 for i in range(len(r))]
    max_index = 0
    max_pos = 0
    left = 0
    max_len = 0
    for i in range(1, len(lens)):
        lens[i] = 1 if i < max_pos else min(lens[2 * max_index - i], max_pos - i)
        while i + lens[i] < len(r) and i - lens[i] > -1 and r[i + lens[i]] == r[i - lens[i]]:
            lens[i] += 1
        if i + lens[i] > max_pos:
            max_index = i
            max_pos = i + lens[i] - 1
        if lens[i] - 1 > max_len:
            max_len = lens[i] - 1
            left = (i - lens[i] + 1) // 2
    return s[left:left + max_len]


def increasingTriplet(nums):
    '''
     334.递增的三元子序列
    给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
    贪心选择
    数学表达式如下:
    如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
    '''
    if len(nums) < 3:
        return False
    h, k = 2 << 30, 2 << 30
    for i in nums:
        if h >= i:  # 如果当前值小于h则更新h,
            h = i
        elif k >= i:  # 如果当前值大于h但是小于k
            k = i
        else:  # 如果当前值大于k就说明 已经找到三个数按大小顺序排列直接返回True
            return True
    return False


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
