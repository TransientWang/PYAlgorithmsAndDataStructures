# -*- coding: UTF-8 -*-
def reverseString(s):
    """
    344. 反转字符串(review)
    :param s:
    :return:
    """
    i = 0
    j = len(s) - 1
    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1