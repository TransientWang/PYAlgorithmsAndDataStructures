# -*- coding: UTF-8 -*-

import math


def isHappy(n):
    '''
    编写一个算法来判断一个数是不是“快乐数”。

    一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
    然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
    需要考虑的是只要出现循环 就判定不是快乐数
    所以可以把之间计算过得数字都保存下来 如果有重复 即为 出现循环
    :param n:
    :return:
    '''
    s = str(n)
    t = 0
    dp = []
    import math
    while True:
        for i in s:
            i = int(i) ** 2
            t += i
        if t == 1:
            return True
        elif dp.count(t) != 0:
            return False
        else:
            dp.append(t)
            s = str(t)
            t = 0


def trailingZeroes(n):
    '''
    给定一个整数 n，返回 n! 结果尾数中零的数量。
    :param n:
    :return:
    '''
    res = 0
    n = n / 5
    while n:
        n = n / 5
        res += 5
    return res


def myPow(x, n):
    '''
    自实现的pow
    :param x:
    :param n:
    :return:
    '''
    if n == 0:
        return 1
    if n < 0:
        return 1.0 / myPow(x, -n)
    if n % 2 == 1:
        return x * myPow(x * x, n // 2)
    else:
        return myPow(x * x, n // 2)


def mySqrt(x):
    '''

    :param x:
    :return:
    '''
    low = 1
    high = x
    while low <= high:
        mid = (low + high) / 2

        if x / mid < mid:
            high = mid - 1
        elif x / mid > mid:
            low = mid + 1
        else:
            return mid
    return low - 1


def majorityElement(nums):
    '''
    求众数
    :param nums:
    :return:
    '''

    count = 1
    t = nums[0]
    for i in range(1, len(nums)):
        if t == nums[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            t = nums[i]
            count = 1
    return t


def evalRPN(tokens):
    '''
    逆波兰表达式求值
    :param tokens:
    :return:
    '''
    stack = []
    while len(tokens) != 0:
        t = tokens.pop(0)
        if t != "+" and t != "-" and t != "*" and t != "/":
            stack.append(t)
        else:
            t2 = stack.pop(-1)
            t1 = stack.pop(-1)
            tmp = eval(str(t1) + str(t) + str(t2))
            stack.append(int(tmp))
    import math
    return int(stack.pop(0))


def divide(dividend, divisor):
    '''

    :param dividend:
    :param divisor:
    :return:
    '''
    if dividend == -2 ** 31 and divisor == -1:
        return 2 ** 31 - 1

    bool = 1
    if dividend > 0:
        bool *= -1
    if divisor > 0:
        bool *= -1
    ded = abs(dividend)
    div = abs(divisor)

    res = 0
    while ded >= div:
        tmp = div
        count = 1
        while ded >= tmp << 1:
            tmp <<= 1
            count <<= 1
        res += count
        ded -= tmp
    return res if bool == 1 else -res


def titleToNumber(s):
    '''
    Excel表列序号
    :param s:
    :return:
    '''
    l = list(s)

    res = 0
    for i in range(len(l)):
        res = res * 26 + ord(l[i]) - 64
    return res


def isPowerOfTwo(n):
    if n == 1:
        return True
    h = 2
    while h < n:
        h *= 2
    return n == h


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def maxPoints(points):
    '''
    hash
    给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
    时间复杂度 o(n)=n²
    两层循环 第一层计算出与每一个点在同一直线上最多的点的个数
    注意的情况有：1、第二层遍历的时候直接遍历原数组就可以，不用单独把这一点排除如果排除增加了复杂性
    2、有垂直于X轴没有斜率的情况，标记一下就可以
    3、在遇到与比较点相同的点的时候（same数量最小也是1 因为比较点没有排除在外）记录下其数量，然后跳过在更新最大值的时候加上就可以
    4、由于精度问题，都转换成浮点数就可以了
    :param points:
    :return:
    '''

    if len(points) == 0:
        return 0
    if len(points) == 1:
        return 1
    r = 0
    for i in range(len(points)):
        res = 0
        dpMap = {}
        p = points[i]
        same = 0
        for point in points:
            if p.x == point.x and p.y == point.y:
                same += 1
                continue
            d = float((p.x - point.x) / (p.y - point.y)) if p.y != point.y else 10000
            if dpMap.get(d) is None:
                dpMap[d] = 1
            else:
                dpMap[d] += 1
            res = max(dpMap[d], res)
        r = max(r, res + same)

    return r


if __name__ == '__main__':
    print(maxPoints([Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]))
    # , Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]
