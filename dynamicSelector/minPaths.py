# -*- coding: UTF-8 -*-
'''
动态规划
'''


def climbStairs(n):
    """
    70.爬楼梯
    分析：
    这道问题属于动态规划的问题
    可以自顶向下看
    假设只有三阶，那么第三阶的走法只有两个，即从倒数第二个上来，和倒数第三个上来。
    那么只要知道了上倒数第二个台阶的走法，和倒数第三个台阶的走法，就可以求出解。
    那么倒数第二个和倒数第三个的走法也可以用一样的步骤去求得。
    可以看出，每一阶的问题只跟前两个台阶有关，那么本来需要一个辅助数组，现在就需要两个变量就可以，
    即：t1+t2=t3
    这里t3可以替换t2,t2可以变成t1，就可以进入下次循环
    这样这个问题就可以看做是一个斐波那契数列
    考察点：动态规划、斐波那契数列
     :type n: int
     :rtype: int
    """
    if n == 1:
        return 1
    t1 = 1
    t2 = 1
    i = 1
    while i <= n:
        t1, t2 = t1 + t2, t1
        i += 1
    return t2


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
            print((res[x][y]), end=' ')
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
        for j in range(0, k):
            if prices[lens - j - 1] > prices[lens - i - 1]:
                cmax = prices[lens - j - 1] - prices[lens - i - 1]
                if cmax > max:
                    max = cmax
    return max


def maxProfit1(prices):
    """
    121. 买卖股票的最佳时机
    :type prices: List[int]
    :rtype: int
    分析：股票只能买入和卖出一次，并且买入在前。
    假设只有两天，设第一天价格为最小值，那么当天买入卖出，收益为0
    接着往下走，第二天如果第二天比第一天价格高，那么结果应该是第二天减去第一天。
    如果第二天比第一天高，那么就显然不能获取收益
    关键点就在于，最小价格，是否在最大价格之前。
    所以当遍历数组的时候，遍历到当前索引时，需要记录从0到该点的最小值，然后如果当前点-最小值，
    比最终收益大，就可以更细，如果小，就说明，前面的最大值，减去前面的最小值，比当前点的解更优，
    所以保存之前的最优解。省去了数组。
    """
    res = 0
    min_val = prices[0]
    for i in (prices):
        min_val = min(min_val, i)
        res = max(i-min_val,res)
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
    if len(cost) == 2:
        return min(cost[0], cost[1])  # 如果只有两个台阶  那么只有一步  跳到代价小的那个台阶上即可
    list = [0 for j in range(len(cost) + 1)]  # 记录从i到j的最小代价，因为要跳出去。所以list的长度要比台阶数+1  list[0] =0 已经包含了只有一个台阶的最优解
    for i in range(2, len(list)):  # 跳到当前台阶上的代价为 从i-1开始跳的还是从i-2开始跳的
        list[i] = min(list[i - 1] + cost[i - 1], list[i - 2] + cost[i - 2])
    return list[i - 1]


'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
一、分析最优解的结构特征  先从自顶向下 分析 加入偷到了最后一家 那么 需要考虑的最大值就是 这家的金额 加上0到i-2户
    能偷到的最大值
    当只有两户的时候只考虑哪家钱多偷哪家的
    当只有一家的时候就偷他家的了
二、递归的定义最优值
    f(n) = d(n) + f(n-2)  ,n>2 
    f(n) = Max(d(0),d(1))   ,n =2 
    f(n) = d(0)            n=1
    
'''


def rob(nums):
    r = [0 for i in range(len(nums))]  # type: List[int] 代表临时最优值
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    r[0] = nums[0]
    r[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        if i == 2:
            r[i] = r[0] + nums[i]
        else:

            print((r[0:i - 2]))
            print((max(r[0:i - 2])))
            r[i] = max(r[0:i - 1]) + nums[i]
    # print(r)
    return max(r)


'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
'''

if __name__ == '__main__':
    print(maxProfit1([7,1,5,3,6,4]))
    pass
