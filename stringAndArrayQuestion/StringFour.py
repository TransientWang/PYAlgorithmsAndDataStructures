# -*- coding: UTF-8 -*-
def reverseWords(s):
    """
    151. 翻转字符串里的单词
    :type s: str
    :rtype: str
    """
    p = list(filter(lambda x: x != "", s.split(" ")))
    p.reverse()
    return " ".join(p)


def compareVersion(version1, version2):
    """
    165. 比较版本号
    :type version1: str
    :type version2: str
    :rtype: int
    """

    def hmap(x):
        t = x.lstrip("0")
        return 0 if t == "" else int(t)

    t = list(map(hmap, version1.split(".")))
    k = list(map(hmap, version2.split(".")))
    j = 0
    for i in range(min(len(t), len(k))):
        if t[i] > k[i]:
            return 1
        elif t[i] < k[i]:
            return -1
        j = i
    if len(t) - len(k) != 0:
        if len(t) > len(k):
            if sum(t[j + 1:]) != 0: return 1
        else:
            if sum(k[j + 1:]) != 0: return -1

    return 0


def findRepeatedDnaSequences(s):
    """
    187. 重复的DNA序列
    :type s: str
    :rtype: List[str]
    """
    exist = set()
    res = []

    for i in range(len(s) - 9):

        if s[i:i + 10] in exist:
            res.append(s[i:i + 10])
        else:
            exist.add(s[i:i + 10])
    return res


def isIsomorphic(s, t):
    """
    205. 同构字符串
    相同的字符串必须被相同的字符替换
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    if len(set(s)) != len(set(t)):
        return False
    table = {}
    for i in range(len(s)):
        if s[i] in table and table[s[i]] != t[i]:
            return False
        else:
            table[s[i]] = t[i]
    return True


def numberToWords(num):
    """
    273. 整数转换英文表示
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "Zero"
    oneNum = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tenNum = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
              "Nineteen"]
    tyNum = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    Num = ["", "Thousand", "Million", "Billion"]
    num = str(num)

    t = []
    p = 0
    h = []
    for i in range(len(num) - 1, -1, -1):
        if p % 3 != 0 or p == 0:
            h.append(num[i])
        else:
            t.append(h[:])
            h = [num[i]]
        p += 1
    if h:
        t.append(h)
    res = ""
    for i in range(len(t)):
        z = ""
        for j in range(len(t[i])):
            if j == 0:
                z += " " + oneNum[int(t[i][j]) - 1]
            elif j == 1:
                m = int(t[i][j] + t[i][j - 1])
                if m > 9 and m < 20:
                    z = " " + tenNum[int(t[i][j - 1])]
                elif m > 19 and int(t[i][j - 1]) == 0:
                    z = " " + tyNum[int(t[i][j]) - 2]
                elif m > 19 and int(t[i][j - 1]) != 0:
                    z = " " + tyNum[int(t[i][j]) - 2] + z
            elif j == 2:
                if int(t[i][0]) + int(t[i][1]) == 0 and int(t[i][2]) != 0:
                    z = oneNum[int(t[i][j]) - 1] + " " + "Hundred"
                elif int(t[i][j]) != 0:
                    z = oneNum[int(t[i][j]) - 1] + " " + "Hundred" + z
                elif int(t[i][0]) + int(t[i][1]) == 0 + int(t[i][2]) == 0:
                    z = ""
        res = " " + z.strip() + " " + Num[i] + res if z != "" else res
    return res.strip()


def hIndex(citations):
    """
    274. H指数
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    citations.reverse()
    p = 0
    for i in range(len(citations)):
        if i <= citations[i] - 1:
            p = i + 1
    return p


if __name__ == '__main__':
    print(hIndex([1]))
