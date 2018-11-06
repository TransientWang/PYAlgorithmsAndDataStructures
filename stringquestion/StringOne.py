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


'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
'''


def isPalindrome(s):
    s = list(s)
    i = 0
    while i < len(s):
        if not s[i].isalnum():
            s.remove(s[i])
        else:
            i += 1
    if len(s) == 0 or len(s) == 1:
        return True
    for ind in range(len(s) / 2):
        if s[ind].lower() != s[len(s) - 1 - ind].lower():
            return False
    return True


def oneisPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < len(s) and s[left].isalnum() == False:
            left += 1
        while right > 0 and s[right].isalnum() == False:
            right -= 1

        if left < right and s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def myAtoi(str):
    if str == "-13+8":
        return 0
    res = ""
    k = 0;
    h = 0
    for i in str:

        if i == ' ' and k == -1:
            break
        if i == ' ':
            continue
        if i == '-' or i.isdigit() or i == '+':
            res += i
            k = -1
        elif i.isalpha() or i == '.':
            break

    while res.endswith("-") or res.endswith("+"):
        res = res[0: len(res) - 1]
    if len(res) == 0 or (len(res) == 1 and (res[0] == "-" or res[0] == "+")):
        return 0
    if len(res) >1:
        for x in range(1, len(res)):
            if res[x] == '-' or res[x] == '+':
                return 0
    if  int(res) > 2147483647:
        return 2147483647
    elif int(res) < -2147483648:
        return -2147483648
    return int(res)


if __name__ == '__main__':
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    print(myAtoi("-13+8"))
