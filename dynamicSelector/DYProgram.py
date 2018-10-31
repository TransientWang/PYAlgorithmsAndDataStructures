# -*- coding: UTF-8 -*-

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]


'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
一、分析最优子结构特征
    当三角形只有一层时 
    triangle[0][0]就是最优值
    当自顶向下看的时候 每一步 都依赖于前一步所选则最优值
    而且前一步的最优值 不一定是下一步选择的最优值
    所以要用而额外空间去存储 从 第一层到 每一层每一节点的最优值
二、递归定义最优值
            if j == 0 :
                r[i][j] = triangle[i][j] + r[i - 1][j]
            elif j == len(triangle[i]) - 1:
                r[i][j] = triangle[i][j] + r[i - 1][j-1]
            else:
                r[i][j] = triangle[i][j] + min(r[i - 1][j], r[i - 1][j - 1])
    
'''


def minimumTotal(triangle):
    if len(triangle) == 1:  # 极端情况  只有一层的时候 返回唯一的一个节点值
        return triangle[0][0]
    lens = len(triangle[len(triangle) - 1])  # 最后一层的长度

    r = [[0 for i in range(lens)] for i in range(lens)]  # 辅助数组  r[i][j]代表从0层到第i层第j节点的最优值
    i, j = 1, 0  # i 代表第i层  j代表第j列
    k = 0  # 遍历每一层求出当层最优值的时候的临时变量
    for t in range(lens):
        r[0][t] = triangle[0][0]
    while i < len(triangle):  # 遍历每一层
        j = 0
        while j < len(triangle[i]):  # 遍历第i层的每一列
            # while k< j:
            # 遍历每一个索引只需要找到 与 它相邻的 上层索引的最优值
            if j == 0:  # 第一个节点 上层邻接节点 只有一个
                r[i][j] = triangle[i][j] + r[i - 1][j]
            elif j == len(triangle[i]) - 1:  # 最后一个节点的 上层邻接节点也只有一个
                r[i][j] = triangle[i][j] + r[i - 1][j - 1]
            else:
                r[i][j] = triangle[i][j] + min(r[i - 1][j], r[i - 1][j - 1])  # 中间节点的上层邻接节点 有两个 需要从两个中
                # 求出最小值
            j += 1
        i += 1
    return min(r[len(triangle) - 1])

'''
两数之和 同一个元素不能被重复利用
'''
def twoSum(nums, target):
    dict={}
    result =[]
    for i in range(len(nums)):
        if dict.get(nums[i]) != None:
            result.append(dict.get(nums[i]))
            result.append(i)
        else:
            dict[target-nums[i]] =i

    return result


if __name__ == '__main__':
    print(twoSum([-10,-1,-18,-19],
-19))



