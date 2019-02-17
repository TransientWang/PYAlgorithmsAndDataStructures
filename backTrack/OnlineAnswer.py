# -*- coding: UTF-8 -*-
# 牛客网上答题样例
# 题目：输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
# 输入描述:
# 每个测试输入包含2个整数,n和m
#
# 输出描述:
# 按每个组合的字典序排列输出,每行输出一种组合


p = input().split(" ")

n = int(p[0])
m = int(p[1])


def dfs(begin, total):
    p = sum(total)

    if p == m:
        # print("".join(total))
        sout = ""
        for idx, i in enumerate(total):
            sout += str(i) + " "
        print(sout.strip())
        return
    for i in range(begin, n + 1):
        s = sum(total)
        if s + i <= m:
            dfs(i + 1, total + [i])


dfs(1, [])

if __name__ == '__main__':
    pass
