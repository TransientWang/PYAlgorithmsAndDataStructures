# -*- coding: UTF-8 -*-
import collections
def singleNumber(nums):
    """
    260. 只出现一次的数字 III
    有两个数只出现了一次记为 num1、num2 初始化为 0, 其余的数出现了两次,
    我们可以对所有的数进行一次异或操作, 易知这个结果就等于 num1 和 num2
    的异或结果(相同的数异或结果都为 0, 0和任意数异或结果都为那个数).

    那么我可以考虑异或结果的某个非 0 位如最后一个非 0 位, 因为我们知道只
    有当 num1、num2 在该位不一样的时候才会出现异或结果为 1. 所以我们以该
    位是否为 1 对数组进行划分, 只要该位为 1 就和 num1 异或, 只要该位为 0
    就和 num2 异或, 这样最终得到就是只出现过一次的两个数(其他在该位为 1 或
    0 的数必然出现 0/2 次对异或结果无影响)
    :type nums: List[int]
    :rtype: List[int]
    """
    num1 = num2 = 0
    xor = 0
    for i in nums:
        xor ^= i
    bit_1 = 1
    while (xor & bit_1) == 0:
        bit_1 <<= 1
    for num in nums:
        if num & bit_1 == 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


def addDigits(num):
    """
    258. 各位相加
    https://en.wikipedia.org/wiki/Digital_root
    例如，11的数字根是2，这意味着11是9之后的第二个数字。
    同样，2035的数字根是1，这意味着2035-1是9的倍数。如果数字产生数字正好9的根，那么数字是9的倍数。
    :type num: int
    :rtype: int
    """

    return (num - 1) % 9 + 1 if num != 0 else 0


def isUgly(num):
    """
    263. 丑数
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False
    dmap = (2, 3, 5)
    if num == 1 or num in dmap:
        return True
    for i in dmap:
        if num % i == 0:
            return isUgly(num // i)
    return False


def nthUglyNumber(n):
    """
    264	.丑数 II
    :type n: int
    :rtype: int
    """
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    for i in range(n - 1):
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min(u2, u3, u5)
        if umin == u2:
            i2 += 1
        elif umin == u3:
            i3 += 1
        elif umin == u5:
            i5 += 1
        ugly.append(umin)
    return ugly[-1]


from heapq import *


def nthSuperUglyNumber(n, primes):
    """
    313. 超级丑数
    :type n: int
    :type primes: List[int]
    :rtype: int
    """

    # res = [1]
    # prime = [0 for i in range(len(primes))]
    # for i in range(n - 1):
    #     p = [res[prime[j]] * primes[j] for j in range(len(prime))]
    #     min_ = min(p)
    #     for k in range(len(prime)):
    #         if p[k] == min_:
    #             prime[k] += 1
    #     res.append(min_)
    # return res[-1]

    heap, uglies, idx, ugly_last = [], [0] * n, [0] * len(primes), [0] * n
    uglies[0] = 1
    for p, k in enumerate(primes):
        heappush(heap, (k, p))
    for i in range(1, n):
        uglies[i], k = heappop(heap)
        ugly_last[i] = k
        idx[k] += 1
        while ugly_last[idx[k]] > k:
            idx[k] += 1
        heappush(heap, (primes[k] * uglies[idx[k]], k))
    return uglies[-1]


def maxProduct(words):
    """
    318. 最大单词长度乘积(review)
    位运算
    通过位运算将重复的找出来
    :type words: List[str]
    :rtype: int
    """

    lookup = collections.defaultdict(int)
    for word in words:
        num = 0  # 因为只有小写字母，所以可以在32位数上表达出来
        for c in word:
            num |= 1 << (ord(c) - ord('a'))  # 将每个字母对位置1，然后跟mask 做或操作，最后的mask就能代表唯一的字符串了
        lookup[num] = max(lookup[num], len(word))

    return max([lookup[x] * lookup[y] for x in lookup for y in lookup if not x & y] + [0])


def bulbSwitch(n):
    """
    319. 灯泡开关（review）
    :type n: int
    :rtype: int
    """
    # 超时做法，解释过程
    # bulb = [1] * n
    # for i in range(2,n+1):
    #     for x in range(i-1, n, i):
    #         bulb[x] = 1 if bulb[x] == 0 else 0
    #     print(bulb,i)
    # return bulb.count(1)
    # 第二种表达
    # p = [i for i in range(1, n + 1) if i ** 0.5 - int(i ** 0.5) == 0]
    # print(p)
    # return len([i for i in range(1, n + 1) if i ** 0.5 - int(i ** 0.5) == 0])
    # 正解
    return int(n ** 0.5)


def countNumbersWithUniqueDigits(n):
    """
    357. 计算各个位数不同的数字个数(review)
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    res = 10
    t = 9
    for i in range(1, n):
        t *= (10 - i)
        res += t
    return res


def isSelfCrossing(x):
    """
    335. 路径交叉
    :type x: List[int]
    :rtype: bool
    """
    for i in range(3, len(x)):
        if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]: return True
        if i >= 4 and x[i - 1] == x[i - 3] and x[i] >= x[i - 2] - x[i - 4]: return True
        if i >= 5 and x[i - 2] >= x[i - 4] and x[i - 3] >= x[i - 1] and x[i - 1] >= x[i - 3] - x[i - 5] and x[i] >= x[
            i - 2] - x[i - 4]: return True
    return False


if __name__ == '__main__':
    print(ord('a') - 97)
