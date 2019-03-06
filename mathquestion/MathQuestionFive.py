# -*- coding: UTF-8 -*-
def isPowerOfFour(self, num):
    """
    342. 4的幂
    num & (num - 1) == 0 只有1个比特为0，
    num & 1431655765 == num
  1431655765 =》  0b1010101010101010101010101010101
    :type num: int
    :rtype: bool
    """
    return num > 0 and num & (num - 1) == 0 and num & 1431655765 == num


def isPowerOfThree(n):
    """
    326. 3的幂（review）
    :type n: int
    :rtype: bool
    """
    while n > 1:
        if n % 3 != 0:
            break
        n /= 3
    return n == 1


def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    """
    365. 水壶问题
    z 能否整除 x  和 y 的最大公约数
    :param self:
    :param x:
    :param y:
    :param z:
    :return:
    """

    if z == 0:
        return True
    if x + y < z:
        return False
    if x > y:
        x, y = y, x
    if x == 0:
        return y == z
    while y % x != 0:
        y, x = x, y % x
    return z % x == 0
