# -*- coding: UTF-8 -*-
import math


def maxProfit(prices):
    """
    review
    122.买卖股票的最佳时机 II
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    这是一个贪心选择问题
    贪心选择有两个性质
       一、贪心选择：原问题的最优解，可以通过一系列局部最优解的选择得到。应用同一规则将原问题变成一个相似但
          规模更小的问题，而后的每一步收拾当前的最佳的选择。这种选择依赖 已作出的选择，但不依赖未作出的选择，
       二、最优子结构：当一个问题的最优解包含其子问题的最优解时，称子问题具有最优子结构性质没问题的最优子结构性质
       是该问题是够可用贪心算法求解的关键
    思路：遍历数组，如果当前值 比上一个值大的话，最大值就加上差，不是就移动向下一位，
    这样连续增长相当于最大值减去最小值。
    有大有小也会把不符合的跳过去了。

    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    valley = prices[0]  # 在前
    peak = prices[0]  # 在后
    sum = 0
    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]  # 先找出一个波谷
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]  # 再找出一个波峰
        sum += peak - valley
    return sum


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    sum = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            sum += prices[i] - prices[i - 1]
    return sum


def findContentChildren(g, s):
    """
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，
    都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。
    如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越
    多数量的孩子，并输出这个最大数值。

     :type g: List[int]
     :type s: List[int]
     :rtype: int
     """
    g.sort()
    s.sort()
    cmin = 0
    ind = 0
    sum = 0
    for i in range(len(s)):
        if s[i] >= g[ind]:
            ind += 1
            sum += 1
            if ind >= len(g):
                break
    return sum


def lemonadeChange(bills):
    """
        在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

    顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

    每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

    注意，一开始你手头没有任何零钱。

    如果你能给每位顾客正确找零，返回 true ，否则返回 false

    问题只跟找钱有关  跟挣多少钱没有关系
    20块钱 不能用于找零
    贪心选择 每次先把 大票找出去
    思路：

    1.记录目前有的钞票数

    2.如果来的人给了5元，直接过，5元钞票数++

    3.如果来的人给了10元，只要至少还有一张5元的，就给过

    4.如果给了20元，优先把10元的钞票退出去（10元钞票只有在这里才能退出去），然后退5元的，退不了就失败

    :type bills: List[int]
    :rtype: bool
    """
    if bills[0] > 5:
        return False
    fmon = 0
    tenmon = 0
    for i in bills:
        if i == 5:  # 给5元不用找
            fmon += 1

        elif i == 10:  # 给10元找一张5元
            tenmon += 1
            if fmon > 0:
                fmon -= 1
            else:
                return False  # 找不了就返回False
        elif i == 20:  # 给20  找15 先能找10元的先找10元，再找5元。 找不了 找3张5元的  找不了就返回
            if tenmon > 0:
                tenmon -= 1
                if fmon > 0:
                    fmon -= 1
                else:
                    return False
            elif fmon >= 3:
                fmon -= 3
            else:
                return False

    return True


def canCompleteCircuit(gas, cost):
    """
    134.加油站
    1. 如果汽车从A开始且无法到达B. A和B之间的任何站点都不能到达B.（B是A无法到达的第一个站点。）
    2. 如果天然气总数大于总成本数。必须有一个解决方案。
    :type gas: List[int]      第i个加油站有汽油gas[i]升
    :type cost: List[int]     从i到i+1需要耗费汽油cost[i]
    :rtype: int
    """
    for i in range(len(gas)):
        p = 0
        k = 0
        for j in range(len(gas)):
            z = i + j
            p += gas[(i + j) % len(gas)]
            if p < cost[(i + j) % len(gas)]:
                k = 1
                break
            p -= cost[(i + j) % len(gas)]
        if k == 0:
            return i
    return -1

def canCompleteCircuit1(gas, cost):
    '''
    134.加油站
    REVIEW
    1. 如果汽车从A开始且无法到达B. A和B之间的任何站点都不能到达B.（B是A无法到达的第一个站点。）
    2. 如果天然气总数大于总成本数。必须有一个解决方案。
    贪心选择解题思路
    一、贪心选择性质：原问题整体最优解 可以通过一系列局部最优的选择得到

        对于加油问题，汽车能否环绕一圈，可以通过选择每一节点能够达到获得
        贪心选择性质就是每次选择是油箱里的油都必须可以到达下一节点，
        下一节点能不能到达 依赖于已经走过的节点后油箱的剩余  而不依赖 没有
        走过的节点
    二、最优子结构
        汽车能否环绕一圈 包含汽车能否达到 i-1,i-2的子问题
    :param gas:
    :param cost:
    :return:
    '''
    if sum(gas) < sum(cost):  # 排除-1的情况
        return -1
    tank, start = 0, 0
    for i in range(len(gas)):  # 一定有解，找到能使油箱油量大于0 的最后一个点
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


def candy(ratings):
    """
    老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

    你需要按照以下要求，帮助老师给这些孩子分发糖果：

    每个孩子至少分配到 1 个糖果。
    相邻的孩子中，评分高的孩子必须获得更多的糖果。

    那么这样下来，老师至少需要准备多少颗糖果呢？


    思路 每个人至少分到一颗糖果
        如果孩子都是按照评分从小到大排序，这时候只需要根据前一个孩子的平评分 跟新当前孩子的评分
        如果是逆序的话 每次更新当前孩子，上上个孩子都会因为上一个孩子的变化 需要重新调整 也就是要回溯
        但是如果我们先只管升序排列的孩子
        然后把逆序的孩子倒过来 那么我们处理的就一直是升序排列的孩子了。想当于处理了一遍就OK了
        :type ratings: List[int]
        :rtype: int
    """
    lens = len(ratings)
    r = [1 for i in range(lens)]

    for x in range(1, lens):
        r[x] = r[x - 1] + 1 if ratings[x] > ratings[x - 1] and r[x] <= r[x - 1] else r[x]
    t = lens - 1
    for x in range(1, lens):
        r[t - x] = r[lens - x] + 1 if ratings[t - x] > ratings[lens - x] and r[t - x] <= r[lens - x] else r[t - x]
    sum = 0
    for q in r:
        sum += q
    return sum


if __name__ == '__main__':
    print((maxProfit([1, 2, 3, 4, 5])))
