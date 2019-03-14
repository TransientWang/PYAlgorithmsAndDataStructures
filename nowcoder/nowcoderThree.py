# -*- coding: UTF-8 -*-|
"""
链接：https://www.nowcoder.com/questionTerminal/bf877f837467488692be703735db84e6
来源：牛客网

牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。


输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
示例1
输入
3 10
1 2 4
输出
8
说明
三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
"""
import sys

n, w = sys.stdin.readline().strip().split()
n = int(n)
w = int(w)
v = map(lambda x: int(x), sys.stdin.readline().split(" "))
v = sorted(v)


def recur(w, v):
    if w == 0 or len(v) == 0:
        return 1
    if v[0] > w:
        return 1
    if v[0] < w:
        return recur(w - v[0], v[1:]) + recur(w, v[1:])
    else:
        return recur(w, v[1:])


if sum(v) <= w:
    print(2 ** n)
else:
    print(recur(w, v))
