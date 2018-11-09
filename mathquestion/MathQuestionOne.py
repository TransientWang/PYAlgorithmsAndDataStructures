# -*- coding: UTF-8 -*-

import math

'''
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
'''


def fizzBuzz(n):
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


'''
质数的个数
埃拉托斯特尼筛法Sieve of Eratosthenes中，
我们从2开始遍历到根号n，先找到第一个质数2，
然后将其所有的倍数全部标记出来，然后到下一个质数3，
标记其所有倍数，一次类推，直到根号n，此时数组中未被标记的数字就是质数。
我们需要一个n-1长度的bool型数组来记录每个数字是否被标记，长度为n-1的原因是题目说是小于n的质数个数，并不包括n。
 然后我们用两个for循环来实现埃拉托斯特尼筛法，难度并不是很大，代码如下所示：
'''


def countPrimes(n):  # TODO 应该再复习
    if n == 0 or n == 1:
        return 0
    dn = math.ceil(math.sqrt(n))
    r = [True for i in range(n - 1)]
    res = 0
    r[0] = False
    for i in range(2, int(dn)):
        if r[i - 1]:
            for j in range(i * i, n, i):
                r[j - 1] = False
    for x in range(n - 1):
        if r[x]:
            res += 1
    return res


def isPowerOfThree(n):
    if n <= 0:
        return False
    maxint = 0x7fffffff
    k = int(math.log(maxint, 3))

    b = 3 ** k

    return b % n == 0


'''
罗马数字转换
'''


def romanToInt(s):
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i == 0 or map[s[i]] <= map[s[i - 1]]:
            result += map[s[i]]
        else:
            result = result + map[s[i]] - 2 * map[s[i - 1]]
    return result


'''
 位1的个数
'''


def hammingWeight(n):
    new_n = bin(n)[2:].zfill(31)
    print(new_n)
    new_n = list(new_n)
    return new_n.count('1')


'''
颠倒二进制位
'''


def reverseBits(n):
    l = list('{0:032b}'.format(n))
    l = list(map(int, l))
    l.reverse()
    l = list(map(str, l))
    s = ''.join(l)
    return int(s, 2)


'''
帕斯卡三角形
用两个数组保存临时结果
数组长度比层数多2
两边置0方便计算
'''


def generate(numRows):
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


'''
有效的括号
用一个栈来保存对应的左括号，如果遇到右括号的时候从栈中弹出一个
因为是按顺序排列的左括号 弹出来的一定是相应的右括号
如果 不相等 就说明 括号没有对称
'''


def isValid(s):
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


if __name__ == '__main__':
    print(isValid("["))
