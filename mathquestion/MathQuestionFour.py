# -*- coding: UTF-8 -*-
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



if __name__ == '__main__':
    pass
    # print(numberToWords(1001))
