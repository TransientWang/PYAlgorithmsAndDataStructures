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
