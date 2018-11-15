# -*- coding: UTF-8 -*-


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


if __name__ == '__main__':
    print(titleToNumber("AB"))
