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


def countPrimes(n): #TODO 应该在复习
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


if __name__ == '__main__':
    print(countPrimes(2))
