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


if __name__ == '__main__':
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
