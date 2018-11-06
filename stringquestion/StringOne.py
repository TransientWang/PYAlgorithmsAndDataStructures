# -*- coding: UTF-8 -*-
import math

'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
在 Integer.max 与 Integer.min 之间
'''
def reverse(x):
    tmp = 0
    strs = ""
    if len(str(abs(x))) < len(str(x)):
        strs += "-"
    for i in range(len(str(abs(x))) - 1):
        tmp = (abs(x) % 10 ** (i + 1) - tmp) / (10 ** i)
        strs +=str(tmp)


    end = abs(x)/ (10 ** (len(str(abs(x)))-1))
    strs += str(end)

    if int(strs) > 2147483647 or int(strs) < -2147483647:
        return 0
    return int(strs)
if __name__ == '__main__':
    reverse(-1230)
