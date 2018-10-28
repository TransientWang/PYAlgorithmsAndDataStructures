# -*- coding: UTF-8 -*-
'''
动态规划
'''


'''
爬楼梯问题
一、最优解的机结构特征
    三种情况
        （1）当只有一阶楼梯时，只有一种解 ：爬一节
        （2）当有两阶楼梯时，有两种解：1、一次爬两阶 2、两次，每次爬一阶
        （3）当有两阶以上时，可以拆分，一下
                                可以先考虑第一步  当一第步走一阶时  还剩下 n-1阶楼梯  求  n-1阶楼梯的走法
                                                  当第一步走两阶时  还剩下  n-2 阶楼梯 求 n-2阶楼梯的走法
                                由此可以看出 当自顶向下看时 n阶台阶的走法 是由n-1阶 + n-2阶走法构成的  
二、根据最优值的特征建立递归算式
       f(n) =  +
               | n=1    ,1
               | n=2    ,2
               | n=3    , f(n-1)+f(n-2)                                                 
'''


def climbStairs(self, n):
    """
     :type n: int
     :rtype: int
    """
    list = [1, 2]
    for i in range(2, n):
        list.append(list[i - 1] + list[i - 2])
    return list[n - 1]


"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。
"""


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    lens = len(s)
    res = 0
    if lens == 0:
        return 0
    if lens == 1:
        return 1
    for i in range(lens):
        if s[lens - i - 1] != " ":
            res += 1
        else:
            return res
    return res





'''
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
'''
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    def uniquePathsSolution(m, n, tm, tn):
        if m == tm and n != tn:
            return uniquePathsSolution(m, n + 1, tm, tn)
        elif n == tn and m != tm:
            return uniquePathsSolution(m + 1, n, tm, tn)
        elif m == tm and n == tn:
            return 1
        return uniquePathsSolution(m + 1, n, tm, tn) + uniquePathsSolution(m, n + 1, tm, tn)

    return uniquePathsSolution(1, 1, m, n)


if __name__ == '__main__':
    print(uniquePaths(3,2))

