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


if __name__ == '__main__':
    print(reverseWords("dc            a"))
