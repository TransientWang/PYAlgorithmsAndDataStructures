# -*- coding: UTF-8 -*-

import math
import random


def fizzBuzz(n):
    '''
    写一个程序，输出从 1 到 n 数字的字符串表示。

    1. 如果 n 是3的倍数，输出“Fizz”；

    2. 如果 n 是5的倍数，输出“Buzz”；

    3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
    '''

    res = []
    for i in range(1, n + 1):
        if i >= 5 and i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
            continue
        if i >= 3 and i % 3 == 0:
            res.append("Fizz")
            continue
        if i >= 4 and i % 5 == 0:
            res.append("Buzz")
            continue
        res.append(str(i))
    return res


def countPrimes(n):  # TODO 应该再复习
    '''
    204	.计数质数
    埃拉托斯特尼筛法（ieve of Eratosthenes)中，
    我们从 2开始遍历到根号n ，先找到第一个质数2，
    然后将其所有的倍数全部标记出来，然后到下一个质数3，
    标记其所有倍数，一次类推，直到根号n，此时数组中未被标记的数字就是质数。
    我们需要一个n-1长度的bool型数组来记录每个数字是否被标记，长度为n-1的原因是题目说是小于n的质数个数，并不包括n。
     然后我们用两个for循环来实现埃拉托斯特尼筛法，难度并不是很大，代码如下所示：
    '''
    if n == 1 or n == 0:
        return 0
    bool = [True for i in range(n - 1)]
    bool[0] = False
    sqrts = math.ceil(math.sqrt(n))
    for i in range(2, int(sqrts)):  # 从2到根号n向下取整
        if bool[i - 1]:
            for j in range(i * i, n, i):  # i的倍数全部都标记
                bool[j - 1] = False
    res = 0
    for i in range(n - 1):
        if bool[i]:
            res += 1
    return res


def isPowerOfThree(n):
    if n <= 0:
        return False
    maxint = 0x7fffffff
    k = int(math.log(maxint, 3))

    b = 3 ** k

    return b % n == 0


def romanToInt(s):
    '''
    罗马数字转换
    '''
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i == 0 or map[s[i]] <= map[s[i - 1]]:
            result += map[s[i]]
        else:
            result = result + map[s[i]] - 2 * map[s[i - 1]]
    return result


def hammingWeight(n):
    '''
    191.位1的个数
    '''
    # new_n = bin(n)[2:].zfill(31)
    # print(new_n)
    # new_n = list(new_n)
    # return new_n.count('1')
    if n == 0:
        return 0
    res = 1
    while n > 2:
        res += n % 2
        n = math.floor(n / 2)
    return res


def reverseBits(n):
    '''
    190.颠倒二进制位
    依次将n的末尾位给result的末尾位，并且result向左移31次
    '''
    # l = list('{0:032b}'.format(n))
    # l = list(map(int, l))
    # l.reverse()
    # l = list(map(str, l))
    # s = ''.join(l)
    # return int(s, 2)
    res = 0
    for i in range(32):
        tmp = n & 1
        n = n >> 1
        res = (res << 1) | tmp
    return res


def generate(numRows):
    '''
    帕斯卡三角形
    用两个数组保存临时结果
    数组长度比层数多2
    两边置0方便计算
    '''
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    res = [[1], [1, 1]]
    dp = [0 for i in range(numRows + 2)]
    new_dp = [0 for i in range(numRows + 2)]
    dp[1] = 1
    dp[2] = 1
    for j in range(2, numRows):
        for k in range(1, j + 2):
            new_dp[k] = dp[k] + dp[k - 1]
        dp = new_dp[:]
        res.append(new_dp[1:j + 2])
    return res


def isValid(s):
    '''
    有效的括号
    用一个栈来保存对应的左括号，如果遇到右括号的时候从栈中弹出一个
    因为是按顺序排列的左括号 弹出来的一定是相应的右括号
    如果 不相等 就说明 括号没有对称
    '''
    dp = []
    for i in s:
        if i == "(":
            dp.append(")")
        elif i == "{":
            dp.append("}")
        elif i == "[":
            dp.append("]")
        elif not dp or dp.pop() != i:
            return False
    return not dp


def missingNumber(nums):
    '''
    缺失的数字
    '''
    t = 0
    tmp = 0
    for i in range(len(nums)):
        t += i
        tmp += nums[i]
    t += len(nums)

    return t - tmp


'''
颠倒二进制位
'''


def hammingDistance(x, y):
    '''
    461.汉明距离
    :param x:
    :param y:
    :return:
    '''
    # l1 = list('{0:032b}'.format(x))
    # l1 = list(map(int, l1))
    # l2 = list('{0:032b}'.format(y))
    # l2 = list(map(int, l2))
    #
    # res = 0
    #
    # for i in range(32):
    #     if l1[i] != l2[i]:
    #         res += 1
    #
    # return res
    res =0
    for i in range(32):
        if (x & (i << i)) ^ (y & (i << i)):
            res +=1
    return res



'''
Shuffle an Array
打乱一个没有重复元素的数组。
'''


class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """

    def reset(self):
        return self.nums
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

    def shuffle(self):
        """
               Returns a random shuffling of the array.
               :rtype: List[int]
               """
        r = []
        tmp = self.nums[:]
        while tmp:
            ran = int(random.uniform(0, len(tmp)))
            r.append(tmp[ran])
            tmp.remove(tmp[ran])
        return r


def sortColors(nums):
    nums.sort()
    return nums


if __name__ == '__main__':
    print(0x01)
    pass
