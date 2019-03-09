# -*- coding: UTF-8 -*-
import sys, collections

if __name__ == '__main__':
    """
    字母交换
    区间动态规划
    https://blog.csdn.net/flushhip/article/details/79416715
    https://www.nowcoder.com/test/question/done?tid=21881021&qid=141023#summary
    【编码题】字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？

    输入描述:
    第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)

    输出描述:
    一个非负整数，表示操作之后，连续最长的相同字母数量。

    输入例子1:
    abcbaa 2

    输出例子1:
    2

    例子说明1:
    使2个字母a连续出现，至少需要3次操作。即把第1个位置上的a移动到第4个位置。
    所以在至多操作2次的情况下，最多只能使2个b或2个a连续出现。
    """
    line, n = sys.stdin.readline().strip().split()
    mp = collections.defaultdict(list)

    for i, val in enumerate(line):
        mp[val].append(i)
    count = 1

    for k, v in mp.items():
        if len(v) <= 1:
            continue
        dp = [[0] * len(v) for i in range(len(v))]
        for lens in range(2, len(v) + 1):
            for begin in range(len(v) - lens + 1):
                end = begin + lens - 1
                dp[begin][end] = dp[begin + 1][end - 1] + (v[end] - v[begin]) - lens + 1

                if dp[begin][end] < int(n):
                    count = max(count, lens)

    print(count)
