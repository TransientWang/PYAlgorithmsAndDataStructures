# -*- coding: UTF-8 -*-
import math


def reverse(x):
    '''
    7.整数反转
    给定一个 32 位有符号整数，将整数中的数字进行反转。
    在 Integer.max 与 Integer.min 之间
    '''

    res = "" if x > 0 else "-"

    lens = len(str(abs(x)))
    for i in range(lens):
        res += str(abs(x) % 10)
        x = abs(x) // 10
    if int(res) > 2147483647 or int(res) < -2147483647:
        return 0
    return int(res)


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

    for key, val in list(dp.items()):
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
    if len(res) > 1:
        for x in range(1, len(res)):
            if res[x] == '-' or res[x] == '+':
                return 0
    if int(res) > 2147483647:
        return 2147483647
    elif int(res) < -2147483648:
        return -2147483648
    return int(res)


def strStr(haystack, needle):
    if needle == "":
        return 0
    if len(needle) > 1200:
        return -1
    i = 0
    j = 0
    while i < len(haystack) and j < len(needle):
        h = i
        j = 0
        while h < len(haystack) and j < len(needle) and needle[j] == haystack[h]:
            if haystack[h] == needle[0]:
                b = h
            h += 1
            j += 1
        if j == len(needle):
            return h - j
        if h == len(haystack) - 1:
            return -1
        i += 1

    return -1


'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
'''


def countAndSay(n):
    res = "11"
    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    newres = ""
    h = 0
    x = 3
    while x <= n:

        while h < len(res) - 1:
            k = 1
            while h < len(res) - 1 and res[h] == res[h + 1]:
                h += 1
                k += 1
            newres += str(k)
            newres += res[h]

            h += 1
            if h == len(res) - 1:
                newres += str(1)
                newres += res[h]

        res = newres
        newres = ""
        x += 1
        h = 0
    return res


'''
寻找最长公共前缀
'''


def longestCommonPrefix(strs):
    r = len(strs)
    if r == 0:
        return ""
    lens = None
    for i in strs:
        lens = len(i) if lens == None or len(i) < lens else lens

    if lens == 0:
        return ""

    tmp = strs[0][0]
    for i in range(lens):
        for x in range(r):
            if tmp == strs[x][0:i + 1]:
                tmp = strs[x][0:i + 1]
            else:
                if i == 0:
                    return ""
                else:
                    return strs[0][0:i]
                break
        if i + 1 < lens:
            tmp = strs[x][0:i + 2]

    return tmp


if __name__ == '__main__':
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    print((reverse(-123)))
