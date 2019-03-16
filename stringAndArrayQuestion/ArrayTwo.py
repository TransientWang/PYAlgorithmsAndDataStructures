# -*- coding: UTF-8 -*-

def gameOfLife(board):
    '''
    289.生命游戏（review）
    状态转换
    0 死细胞到死细胞
    1 活细胞到活细胞
    2 活细胞到死细胞
    3 死细胞到活细胞
    :param board:
    :return:
    '''
    vector = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            count = 0
            for vec in vector:
                x = i + vec[0]
                y = j + vec[1]
                if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0:
                    continue
                elif board[x][y] == 1 or board[x][y] == 2:
                    count += 1
            if board[i][j] and (count < 2 or count > 3):
                board[i][j] = 2
            elif not board[i][j] and count == 3:
                board[i][j] = 3
    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] %= 2


def containsDuplicate(nums):
    """
     review
     217.存在重复
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
    思路：除了hash空间换时间，就是先排序再找了
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1:
        return False
    res = 0
    nums.sort()
    for i in nums:

        if res ^ i == 0:
            return True
        res = i
    return False


def containsNearbyDuplicate(nums, k):
    """
    219. 存在重复元素 II
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
    思路：索引 i,j差绝对值不大于k，且nums[i] ==nums[j] 那么考察的范围最多在K。所以可以维护一个 滑动窗口
    元素数量大于k的时候把最左边的删除
    考察：滑动窗口
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) < 2:  # 这几行过滤了大量的情况。
        return False
    if len(nums) == len(set(nums)):
        return False

    tp = set()  # 防止重复元素过高，造成超时
    for i, num in enumerate(nums):
        if num in tp:
            return True
        tp.add(num)
        if len(tp) > k:
            tp.remove(nums[i - k])


if __name__ == '__main__':
    pass
