# -*- coding: UTF-8 -*-

import math


def isHappy(n):
    '''
    202.快乐数
    编写一个算法来判断一个数是不是“快乐数”。

    一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
    然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
    需要考虑的是只要出现循环 就判定不是快乐数
    所以可以把之间计算过得数字都保存下来 如果有重复 即为 出现循环
    :param n:
    :return:
    '''
    s = str(n)
    dMap = []
    while s != "1":
        if s in dMap:
            return False
        else:
            dMap.append(s)
        r = 0
        for i in s:
            r += int(i) ** 2
        s = str(r)
    return True


def trailingZeroes(n):
    '''
    172.阶乘后的零
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
    50.自实现的pow
    :param x:
    :param n:
    :return:
    '''
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1.0 / myPow(x, -n)
    if n % 2 == 1:
        return x * myPow(x ** 2, n >> 1)
    else:
        return myPow(x ** 2, n >> 1)


def mySqrt(x):
    '''
    69.x 的平方根(牛顿迭代法)
    其他解法：对于一个非负数n，它的平方根不会小于大于（n/2+1）
    :param x:
    :return:
    '''
    # low = 1
    # high = x
    # while low <= high:
    #     mid = (low + high) / 2
    #     if x / mid < mid:
    #         high = mid - 1
    #     elif x / mid > mid:
    #         low = mid + 1
    #     else:
    #         return mid
    # return low - 1
    if x == 0:
        return 0
    last = 0
    res = 1
    while abs(res - last) > 1e-6:
        last = res
        res = (res + x / res) / 2
    return int(res)


def majorityElement(nums):
    '''
    169.求众数
    :param nums:
    :return:
    '''
    count = 0
    tmp = 0

    for num in nums:
        if count == 0:
            tmp = num
        if tmp == num:
            count += 1
        else:
            count -= 1
    return tmp


def getSum(a, b):
    """
    371.两整数之和
    32 bits integer max
    MAX = 0x7FFFFFFF == 2147483647
    32 bits interger min
    MIN = 0x80000000
    int -1 的补码 0xFFFFFFFF
    :param self:
    :param a:
    :param b:
    :return:
    """
    while b:
        a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
    return a if a < 0X7fffffff else ~(a ^ 0xFFFFFFFF)


def evalRPN(tokens):
    '''
    150	.逆波兰表达式求值
    :param tokens:
    :return:
    '''
    stack = []
    for k in tokens:
        if k != "+" and k != "-" and k != "*" and k != "/":
            stack.append(int(k))
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            tmp = eval(str(t2) + str(k) + str(t1))
            stack.append(int(tmp))

    return stack.pop()


def divide(dividend, divisor):
    '''
    29.两数相除
    :param dividend:majorityElement
    :param divisor:
    :return:
    '''
    if dividend == -2 ** 31 and divisor == -1:
        return 2 ** 31 - 1

    bool = (divisor > 0) ^ (dividend > 0)
    dnd = abs(dividend)
    dor = abs(divisor)
    res = 0
    while dnd >= dor:
        t = dor
        count = 1
        while dnd >= (t << 1):
            count <<= 1
            t <<= 1
        res += count
        dnd -= t
    return res if not bool else -res


def titleToNumber(s):
    '''
    171.Excel表列序号
    :param s:
    :return:
    '''
    res = 0
    for i in s:
        res = res * 26 + ord(i) - 64
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


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def largestNumber(nums):
    '''
    考察排序 贪心思想
    关键在于排序的规则
    考虑：如果位数相同的话，那么大的肯定应该在高位
    如果位数不同，高位数大的也应该在前面。需要解决的问题就是位数不同的问题
    解决办法就是，正反concat两个被排序的数字（a+b,b+a)，比较这两个数就相当于比较两个位数相同的数字了
    最大数
    :param nums:
    :return:
    '''
    res = ""
    from functools import cmp_to_key
    comp = cmp_to_key(lambda a, b: int(b + a) - int(a + b))
    return "".join(sorted(map(str, nums), key=comp)).lstrip("0") or "0"


if __name__ == '__main__':
    print(getSum(11, 23))
    print( ~(-2147483649^0xFFFFFFFF))

    # , Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]
