# -*- coding: UTF-8 -*-
import math

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
这是一个贪心选择问题
贪心选择有两个性质  
   一、贪心选择：原问题的最优解，可以通过一系列局部最优解的选择得到。应用同一规则将原问题变成一个相似但
      规模更小的问题，而后的每一步收拾当前的最佳的选择。这种选择依赖 已作出的选择，但不依赖未作出的选择，
   二、最优子结构：当一个问题的最优解包含其子问题的最优解时，称子问题具有最优子结构性质没问题的最优子结构性质
   是该问题是够可用贪心算法求解的关键
   
'''


def maxProfit(prices):
    """
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
    cur = prices[0]
    sum = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            sum += prices[i] - prices[i - 1]
    return sum


'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，
都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。
如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越
多数量的孩子，并输出这个最大数值。
'''


def findContentChildren(g, s):
    """
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


'''
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


'''


def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    if bills[0] > 5:
        return False
    fmon = 0
    tenmon = 0
    for i in bills:
        if i == 5: #给5元不用找
            fmon += 1

        elif i == 10: # 给10元找一张5元
            tenmon +=1
            if fmon > 0:
                fmon -=1
            else:
                return False #找不了就返回False
        elif i ==20:  #给20  找15 先能找10元的先找10元，再找5元。 找不了 找3张5元的  找不了就返回
            if tenmon >0:
                tenmon -=1
                if fmon >0:
                    fmon-=1
                else:
                    return False
            elif fmon >=3:
                fmon-=3
            else:
                return False

    return True


if __name__ == '__main__':
    print(lemonadeChange([5,5,10,10,20]))
