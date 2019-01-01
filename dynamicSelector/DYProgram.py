# -*- coding: UTF-8 -*-

def findKthLargest(nums, k):
    """
    215	.数组中的第K个最大元素
    思路：分治思想+快速排序
    快排一次，如果哨兵位置 ==k 直接返回
    如果哨兵位置大于k说明第k个元素应该从左边找，反之从右边找
    如果数量非常大，可以用堆
    :param nums:
    :param k:
    :return:
    """

    def swap(nums, i, j):
        t = nums[j]
        nums[j] = nums[i]
        nums[i] = t

    def find(left, right):
        if left > right:
            return
        tmp = nums[left]
        i = left
        j = right
        while i < j:
            while i < j and nums[j] < tmp:  ##注意是左边最大，应该从右边开始找
                j -= 1
            while i < j and nums[i] >= tmp:
                i += 1

            if i < j:
                swap(nums, i, j)
        nums[left] = nums[i]
        nums[i] = tmp

        return i

    def search(left, right, k):
        m = find(left, right)
        print(nums)
        if m - left + 1 == k:
            return nums[m]
        elif k < m - left + 1:
            return search(left, m - 1, k)
        else:
            return search(m + 1, right, k - (m - left + 1))

    return search(0, len(nums) - 1, k)


def minimumTotal(triangle):
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


def maxCoins(nums):
    '''
    TODO 此题目比较难，多回顾
    312.戳气球
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。
    注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。
    测试用例：3,1,5,8
    '''

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


def isValidSudoku(board):
    '''
    判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    '''
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
            for xx in range(x * 3, x * 3 + 3):
                for yy in range(y * 3, y * 3 + 3):
                    if board[xx][yy] != "." and dp2[int(board[xx][yy])] == 0:
                        dp2[int(board[xx][yy])] = 1
                    elif board[xx][yy] != ".":
                        return False

    return True


def numSquares(n):
    '''
    279	.完全平方数
    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
    这个方法超时
    :param n:
    :return:
    '''
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    dp = [2 ** 31 for i in range(n + 1)]  # dp[i]表示i最少平方和个数
    dp[0] = 0

    for i in range(n + 1):
        for j in range(1, n + 1):
            if i + j * j > n:
                break
            dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])

    return dp[-1]


def numSquaresOne(n):
    '''
    279	.完全平方数
    四平方和定理
    根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，
    那么就是说返回结果只有1,2,3或4其中的一个，首先我们将数字化简一下，由于一个数如果含有因子4，
    那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同，读者可自行举更多的栗子。
    还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
    :param n:
    :return:
    '''
    import math
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    n = int(n)
    i = 0
    while i ** 2 <= n:
        b = int(math.sqrt(n - i ** 2))
        if i ** 2 + b ** 2 == n:
            return 1 if 0 in [i, b] else 2
        i += 1

    return 3


if __name__ == '__main__':
    print(numSquaresOne(12))
