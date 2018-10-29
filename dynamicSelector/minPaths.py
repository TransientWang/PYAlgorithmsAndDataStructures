# -*- coding: UTF-8 -*-
'''
动态规划
'''

'''
爬楼梯问题
一、最优解的结构特征
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

一、最优解的结构特征
    
    
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


'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
一、分析最优解的结构特征
    假设极端情况  当只有一行一列时  最优解就是grid[0][0]
    有一行或者一列时 最优解 就是 这一行或者一列的和
    在多行多列的情况时从自顶点向下来看 到每个点的最小距离为能到达它的两个前顶点中最小的一个解
'''


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    res = [[0 for aa in range(len(grid[0]))] for bb in range(len(grid))]
    res[0][0] = grid[0][0]

    for i in range(1, len(grid[0])):
        res[0][i] = grid[0][i] + res[0][i - 1]
    for j in range(1, len(grid)):
        res[j][0] = grid[j][0] + res[j - 1][0]
    for x in range(1, len(grid)):
        for y in range(1, len(grid[0])):
            res[x][y] = res[x - 1][y] + grid[x][y] if res[x - 1][y] < res[x][y - 1] else res[x][y - 1] + grid[x][y]
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            print(res[x][y]),
        print("\n")
    return res[len(grid) - 1][len(grid[0]) - 1]


'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
一、分析问题的最优子结构特征
        极端情况数组长度为1代表只有1天股票交易  那么最大收益为0
        普通情况买进 日一定比卖出日小 才有肯能获得收益
        重叠的子问题就是 最小买进 

'''


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    lens = len(prices)
    max = 0  # 有没有一个初始值？
    cmax = 0
    for i in range(len(prices)):
        k = i + 1
        for j in range(0,k):
            if prices[lens - j - 1] > prices[lens - i - 1]:
                cmax = prices[lens - j - 1] - prices[lens - i - 1]
                if cmax > max:
                    max = cmax
    return max
'''
TODO此问题应该在看看
'''


def maxProfit1(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if prices == None or len(prices) ==0:
        return 0
    Min = prices[0] #最小的时候买入
    res =0 #结果
    for i in prices:
        Min = min(Min, i)  # 遍历到目前为止 Min总是最小值
        res = max(res, i - Min)  # i-Min代表当前值减去当前最小值的一个比较 注意 当前最小值的索引一直在当前遍历位置之后
        # 也就是代表当前卖出减去最小买入

    return res


'''
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
当索引位置为0的时候不耗费体力  跳过
一、最优解的结构特征
    当只有一个台阶时 则直接到达顶点 不用耗费代价
    当只有两个台阶时 必须调到一个台阶上  则跳到一个最小的代价就可以
    因为每次可以跳一步或者两步  所以可以考虑问题 为 跳一步+之前的代价  与 跳两步+之前的代价的最小者
二、递归的定义最优值
    list[i] = min(list[i - 1] + cost[i-1], list[i - 2]+ cost[i-2])
三、以自底向上的方式求出最优值
'''


def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    if len(cost) ==2:
        return min(cost[0], cost[1]) #如果只有两个台阶  那么只有一步  跳到代价小的那个台阶上即可
    list = [0 for j in range(len(cost)+1)]  # 记录从i到j的最小代价，因为要跳出去。所以list的长度要比台阶数+1  list[0] =0 已经包含了只有一个台阶的最优解
    for i in range(2,len(list)):  #跳到当前台阶上的代价为 从i-1开始跳的还是从i-2开始跳的
        list[i] = min(list[i - 1] + cost[i-1], list[i - 2]+ cost[i-2])
    return list[i-1]


if __name__ == '__main__':
    print(minCostClimbingStairs([0,0,1,1]))
