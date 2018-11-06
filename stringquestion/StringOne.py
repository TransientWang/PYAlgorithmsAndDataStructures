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
        strs += str(tmp)

    end = abs(x) / (10 ** (len(str(abs(x))) - 1))
    strs += str(end)

    if int(strs) > 2147483647 or int(strs) < -2147483647:
        return 0
    return int(strs)


'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
'''


def firstUniqChar(s):
    if len(s) == 0:
        return -1
    ss = list(s)

    dp = {}
    for st in ss:
        if dp.get(st) == None:
            dp[st] = 0
        else:
            dp[st] = 1
    res = len(s)

    for key, val in dp.items():
        if val == 0:
            res = s.index(key) if s.index(key) < res else res
    if res == len(s):
        return -1
    return res

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
'''
def isAnagram(s, t):
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    for i in range(len(ss)):
        if ss[i] != tt[i]:
            return False
    return True
if __name__ == '__main__':
    print(isAnagram("aacc"))
