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
if __name__ == '__main__':
    print(trailingZeroes(1808548329))
