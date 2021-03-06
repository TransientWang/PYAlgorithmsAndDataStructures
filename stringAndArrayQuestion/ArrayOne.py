# -*- coding: UTF-8 -*-
def productExceptSelf(nums):
    '''
    3238.除自身以外数组的乘积（reveiw）
    给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    :param nums:
    :return:
    '''
    r = [1 for i in range(len(nums))]
    r1 = [1 for i in range(len(nums))]
    output = [1 for i in range(len(nums))]
    for i in range(len(nums) - 1):
        r[i + 1] = nums[i] * r[i] if i >= 0 else nums[i]

    for i in range(1, len(nums)):
        r1[i] = nums[-i] * r1[i - 1] if i >= 0 else nums[-i]
    r1.reverse()
    for i in range(len(nums)):
        output[i] = r[i] * r1[i]
    return output


    # 二
    p = 1
    out = []
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = p * out[i]
        p *= nums[i]
    return out


def spiralOrder(matrix):
    '''
    54.螺旋矩阵
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    思路：这个问题 需要考虑的方面有两个，一个是遍历的方向，另一个是每一方向遍历的步数，
    方向可以有四个，步数每一方向走完，下次在走这个方向的时候就会减少一
    :param matrix:
    :return:
    '''
    row = len(matrix) - 1
    if row == -1:
        return matrix
    if row == 0:
        return matrix[0]
    column = len(matrix[0])
    map = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 记录方向
    vector = 0  # 标记方向
    x = 0
    y = -1
    res = []
    while row >= 0 and column > 0:  # 将横向和走向放在一起走，注意横向步数条件是 >0
        for i in range(column):  # 走横向
            x += map[vector % 4][0]
            y += map[vector % 4][1]
            res.append(matrix[x][y])
        vector += 1
        for j in range(row):  # 走纵向
            x += map[vector % 4][0]
            y += map[vector % 4][1]
            res.append(matrix[x][y])
        vector += 1
        row -= 1
        column -= 1
    return res


def firstMissingPositive(nums):
    '''
    41. 缺失的第一个正数
    将找到的元素放到正确的位置，如果发现某个元素一直没找到，则该元素即为所求

    循环不变式：如果某命题初始为真，且每次改变后仍保持该命题为真，则若干次改变后该命题为真
    只允许时间复杂度O(n)的算法，并且只能使用常数级别的空间。

    分析：把当前数放到该放的位置即可，如1应该放到第0个位置，2应该放到第1个位置。
        :param nums:
    :return:
    '''
    for i in range(len(nums)):
        while 0 <= nums[i] - 1 < len(nums) and nums[i] != nums[nums[i] - 1]:
            idx = nums[i] - 1
            nums[i], nums[idx] = nums[idx], nums[i]

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1
    return len(nums) + 1


def longestConsecutive(nums):
    '''
    128.最长连续序列
    给定一个未排序的整数数组，找出最长连续序列的长度。

    要求算法的时间复杂度为 O(n)。
    思路：用hashMap 存储数字个数字坐在序列的长度
    排除出现重复数字的情况
    一、当数字 i-1 在map中的时候 取map[i-1]的值left
    二、当数字 i+1 在map中的时候 去map[i+1]的值right
    此时数字i的值就是 left+right+1
    三、但是还有一种情况就是数字 i在序列的最左边 或最右边
    这时候map[i+1]或map[i-1]的值就不是此序列的最长值了
    所以可以 借助left和right 找到 此序列的端点值 map[i-left] map[i+eight]
    将这两点也更新 就能保证正确
    :param nums:
    :return:
    '''
    dpMap = {}
    res = 0
    for i in nums:
        if i not in dpMap:
            left = 0
            right = 0
            if i + 1 in dpMap.keys():
                right = dpMap[i + 1]
            if i - 1 in dpMap.keys():
                left = dpMap[i - 1]
            if left != 0 or right != 0:
                dpMap[i] = left + right + 1
                dpMap[i - left] = dpMap[i]
                dpMap[i + right] = dpMap[i]
            else:
                dpMap[i] = 1
        res = max(res, dpMap[i])
    print(dpMap)
    return res


def findDuplicate(nums):
    '''

    287.寻找重复数(review)
    如果数组的每一个数的取值都是不重复的，那么可以选取特定的数值来使，不断通过索引值得到数值，再将新的数值作为索引值，循环下去可以得到一个链路。假定数组为[1,2,3,4,5]，设定f(x)，x是索引值，f(x)是值，并将得到的f(x)作为下一个输入，这样形成了一个链路，1->2->3->4->5；但是如果稍微做一下改变原数组为[1,2,3,4,1]，那么链路将变为，1->2->3->4->1…，形成一个环路，这里的重复数字1就是构成环路的关键。
    本题中就包含这样一个重复数字，所以数组nums一定会存在一个环路，问题变为如何查找环路起点问题，对于这种问题有这样一个算法，叫做弗洛伊德的循环寻找算法。在算法中会有两个指针一个快速指针每次移动两个步骤，一个慢速指针每次移动一个步骤，其中快速指针会提前进入循环并且在慢速指针进入循环后会与其相交。类似于操场跑圈，快速指针和慢速指针同时同宿舍出发，快速指针先到操场开始跑圈，慢速指针后到操场开始跑圈，但是快速指针一定会在某个时刻与慢速指针到达同一位置。
    如何求取圆环起点位置（即重复的数字）：
    设定慢速指针与快速指针相交点距离环起点的距离为k，环周长为n，指针起点到环起点的距离为m，则慢速指针走过的距离为a = m+k+xn ；快速指针走过的距离为2a = m+k+yn，两者做差可以得到a = (y-x)n，是环长度的整数倍，如果将快速指针重置到起点，且将快速指针的移动距离改为1，那么当快速指针移动到圆环起点时，慢速指针移动距离为a+m，因为a是圆环长度的整数倍，所以慢速指针的位置也是在圆环起点，这样两者的相遇点即为圆环起点。
    周长-k=m
    图：--○
    :param nums:
    :return:
    '''
    slow, fast, t = 0, 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while True:
        slow = nums[slow]
        t = nums[t]
        if slow == t:
            break
    return slow


def maxSlidingWindow(nums, k):
    """
    239. 滑动窗口最大值(review)
    deque 左边保存窗口中最大值的索引
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums or len(nums) == 0:
        return
    deque = []
    for i in range(k):  # 初始化，将队列左边变为第一个窗口最大值的索引
        while deque and nums[i] > nums[deque[-1]]:
            deque.pop()
        deque.append(i)
    res = []
    for i in range(k, len(nums)):
        res.append(nums[deque[0]])  # 将索引中的最大值添加到队列中
        if deque[0] < i - k + 1:  # 如果窗口中的最左侧索引已经超出范围则弹出
            deque.pop(0)
        while deque and nums[i] > nums[deque[-1]]:  # 如果新值比窗口中的最大值大则将，窗口中的最大值弹出
            deque.pop()
        deque.append(i)  # 将当前值入队
    res.append(nums[deque[0]])  # 还剩下一个
    return res


def largestRectangleArea(heights):
    '''
    84.柱状图中最大的矩形
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    思路：如果是一个递增的序列那么，最大值可以为 max(heights[i]*len(heights)) heights.pop(0)
    如果不是递增，不好找到规律。
    所以需要构建出这个递增序列。
    从heights[0]开始，当heights[1]比heights[0]大的时候，可以不用着急求出最大值，如果比heights[0]小，
    那么就需要记录前面比heights[0]高的矩形的最大值，然后将他们都消减成与heights[1]一般高，才符合递增。
    这就需要用到栈
    :param heights:
    :return:
    '''
    # stack = []
    # res = 0
    # for height in heights:
    #     t = 1
    #     while len(stack) != 0 and height < stack[-1]:  # 当前值比前面小的时候
    #         res = max(res, stack.pop() * t)  # 求出前面的最大值
    #         t += 1
    #     while t >= 1:  # 将消峰的所有值入栈
    #         stack.append(height)
    #         t -= 1
    #
    # while len(stack) != 0:  # 计算栈中的值
    #     res = max(res, stack[0] * len(stack))
    #     stack.pop(0)  # 将最矮的出栈
    # return res
    # 更快的解
    l = len(heights)
    if l == 0:
        return 0
    if len(set(heights)) == 1:
        return l * heights[0]
    heights.append(0)
    stack, ans = [-1], 0  # stack存储heights[i]的索引
    for i in range(l + 1):
        while heights[i] < heights[stack[-1]]:  # 如果比当前的高度比栈顶的高度大
            h = heights[stack.pop()]  # 从后王往前记录面积
            w = i - stack[-1] - 1  # 宽度
            ans = max(ans, h * w)
        stack.append(i)  # 有序的位置入栈
    return ans


def maximalRectangle(matrix):
    """
    85. 最大矩形
    84题的拓展，从第一行开始记录 所有  1 的高度。
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0  # 记录高度，然后调用84题解，求出最大值
        stack = [-1]
        for i in range(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
