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
    # for t in range(lens):
    r[0][0] = triangle[0][0]
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
        print(r)
    return min(r[len(triangle) - 1])


'''
两数之和 同一个元素不能被重复利用
'''


def twoSum(nums, target):
    dict = {}
    result = []
    for i in range(len(nums)):
        if dict.get(nums[i]) != None:
            result.append(dict.get(nums[i]))
            result.append(i)
        else:
            dict[target - nums[i]] = i

    return result


'''
    
戳气球     
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
这里的 left 和 right 代表和 i 相邻的两个气球的序号。
注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。
测试用例：3,1,5,8
'''


# TODO 此题目比较难，多回顾
def maxCoins(nums):
    nums.append(1)
    nums.insert(0, 1)  # 在数组前面后面加上 1 计算方便
    r = [[0 for z in range(len(nums))] for z in range(len(nums))]  # r[i][j]表示第i和j气球之间的气球戳烂 能得到的最大硬币数量
    orlen = len(nums) - 2  # 原数组长度
    for length in range(1, orlen + 1):  # 计算的每一子问题的长度
        for head in range(1, orlen - length + 1 + 1):  # 子问题的起始点
            tail = head + length - 1  # 子问题的结束点
            for point in range(head, tail + 1):  # 子问题中间的戳气球的点
                ocorn = r[head][tail]  # 子问题原最大值
                latercoin = r[head][point - 1] + r[point + 1][tail] + nums[head - 1] * nums[point] * nums[tail + 1]
                # 子问题当前值  head到Tail都被戳破后 每个被戳破点的能对换硬币值
                r[head][tail] = max(ocorn, latercoin)  # 更新最优值

    return r[1][len(nums) - 2]

'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
'''
def isValidSudoku(board):
    # dp = [[None for i in range(len(board))] for i in range(len(board))]

    for x in range(len(board)):
        dp = [0 for i in range(10)]
        dp1 = [0 for i in range(10)]
        for y in range(len(board)):
            if board[x][y] != "." and dp[int(board[x][y])] == 0:
                dp[int(board[x][y])] = 1
            elif board[x][y] != ".":
                return False
            if board[y][x] != "." and dp1[int(board[y][x])] == 0:
                dp1[int(board[y][x])] = 1
            elif board[y][x] != ".":
                return False
    for x in range(3):
        for y in range(3):
            dp2 = [0 for i in range(10)]
            for xx in range(x * 3, x * 3 +3):
                for yy in range(y * 3, y * 3 +3):
                    if board[xx][yy] != "." and dp2[int(board[xx][yy])] == 0:
                        dp2[int(board[xx][yy])] = 1
                    elif board[xx][yy] != "." :
                        return False

    return True


if __name__ == '__main__':
    print(isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
