# -*- coding: UTF-8 -*-
import math

import copy
from dataStructure import TrieNode


class play(object):
    '''n皇后问题'''
    count = 0  # 结果数量
    n = 8;  # 皇后数量
    x = [0]  # x[i]表示第i个皇后在第几列

    def place(self, t):

        ok = True
        for i in range(0, t):
            if self.x[i] == self.x[t] or math.fabs(t - i) == math.fabs(self.x[t] - self.x[i]):
                ok = False
                break
        return ok

    # t是层数
    def backTrack(self, t):
        if t >= self.n:
            self.count += 1
            for i in range(0, len(self.x)):
                print((self.x[i] + 1), end=' ')
            print('\n')
        else:
            # j是列数
            for j in range(0, self.n):
                self.x[t] = j
                if self.place(t):
                    self.backTrack(t + 1)


def permute(nums):
    '''
    46.全排列
    给定一个没有重复数字的序列，返回其所有可能的全排列。
    BFS:分支线界限法，一般由一个循环开始回溯
    '''
    res = []
    if len(nums) == 1:
        return [nums]

    def backTrack(before, nums):
        now = before[:]
        if len(nums) == 1:
            now.append(nums[0])
            res.append(now)
        else:
            for i in range(len(nums)):
                now.append(nums[i])
                backTrack(now, nums[0:i] + nums[i + 1:])
                now.pop()

    for i in range(len(nums)):
        backTrack([nums[i]], nums[:i] + nums[i + 1:])

    return res


def permuteOne(nums):
    """
    46.全排列
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        num = nums[i]
        sub = permuteOne(nums[:i] + nums[i + 1:])  # 子序列的组个
        for j in sub:
            res.append([num] + j)
    return res


def subsets(nums):
    """
    78.子集
    和全排列基本一致
    :param nums:
    :return:
    """
    res = [[]]
    for i in range(len(nums)):
        sub = subsets(nums[i + 1:])
        for j in sub:
            t = [nums[i]] + j
            res.append(t)
    return res


def exist(board, word):
    '''
    79.单词搜索
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，
    其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    思路：回溯法，剪枝条件为 边界值 和 当前位置的值 是否是word[i]的值
    同时将已遍历过的索引设置一个标记让防止重复遍历 在遍历完四周还要恢复
    :param board:
    :param word:
    :return:
    '''
    row = len(board)
    colum = len(board[0])

    def find(x, y, i):
        if x < 0 or y < 0 or x > row - 1 or y > colum - 1 or board[x][y] != word[i]:
            return False
        t = board[x][y]
        if i == len(word) - 1 and t == word[i]:
            return True
        board[x][y] = 0
        bool = find(x + 1, y, i + 1) or find(x - 1, y, i + 1) or find(x, y + 1, i + 1) or find(x, y - 1, i + 1)
        board[x][y] = t
        return bool

    for i in range(row):
        for j in range(colum):
            if board[i][j] == word[0]:
                if find(i, j, 0):
                    return True

    return False


def existOne(board, word):
    """
    79.单词搜索
    :param board:
    :param word:
    :return:
    """

    def find(x, y, tmp):
        if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0])):
            return False
        tmp += board[x][y]
        if word[:len(tmp)] != tmp:
            return False
        elif tmp == word:
            return True
        t = board[x][y]
        board[x][y] = "."
        bool = find(x + 1, y, tmp) or \
               find(x - 1, y, tmp) or \
               find(x, y + 1, tmp) or \
               find(x, y - 1, tmp)
        board[x][y] = t
        return bool

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and find(i, j, ""):
                return True
    return False


def findWords(board: list, words: list):
    '''
    212.单词搜索二
    正确解法是 前缀树 + DFS
    :param board:
    :param words:
    :return:
    '''
    row = len(board)
    colum = len(board[0])
    res = set()

    def find(x, y, word, TrieNode):
        if x >= 0 and x < row and y >= 0 and y < colum and board[x][y] in TrieNode:
            TrieNode = TrieNode[board[x][y]]
            word += board[x][y]
            if TrieNode.get("#", 9) == True:
                res.append(word)
            t = board[x][y]
            board[x][y] = 3
            find(x + 1, y, word, TrieNode)
            find(x - 1, y, word, TrieNode)
            find(x, y + 1, word, TrieNode)
            find(x, y - 1, word, TrieNode)
            board[x][y] = t

    root = TrieNode.Trie()
    tmp = set()
    for i in words:
        root.insert(i)
        tmp.add(i[0])
    for i in range(row):
        for j in range(colum):
            if board[i][j] in tmp:
                find(i, j, "", root.root)

    return res


def isMatch(s, p):
    """
    TODO 好好看看
    44.通配符
    思路：贪心算法。
    问题的关键在于’*’,而不是’?’。因为’?’只能与单个字符匹配。
    而’*’可以不匹配任何字符或者匹配一个或多个。

    贪心原则为: 先假设 * 只匹配0个字符，此时应记住p索引的位置，然后往下继续匹配。若匹配不成功，则回来，让’‘匹配1个字符，然后继续匹配。。。。以此重复。匹配字符数逐渐+1
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    :type s: str
    :type p: str
    :rtype: bool
    """
    pass
    len_p = len(p)
    len_s = len(s)
    s_index = 0  # 字符串遍历起始索引
    p_index = 0  # 模式串的遍历起始索引
    s_start = 0  # 在遇到*的时候的
    p_start = -1  # 在遇到*
    while s_index < len_s:
        if p_index < len_p and p[p_index] == "*":  # 如果遇到了 * ，那么记录当前遇到 * 时候s和p的索引位置
            p_start = p_index
            p_index += 1  # p_index后移一位，尝试匹配 * 匹配0长度字符是否成功
            s_start = s_index
        elif p_index < len_p and (p[p_index] == "?" or p[p_index] == s[s_index]):
            p_index += 1
            s_index += 1
        elif p_start > -1:  # 如果p_index>0说明曾经碰见过 *，并且 * 尝试匹配之前（有可能是0,1……）的长度字符不成功，
            s_start += 1  # 尝试将 * 匹配长度增加1
            s_index = s_start  # 重新记录起始字符索引的位置
            p_index = p_start
        else:
            return False
    for i in range(p_index, len_p):
        if p[i] != "*":
            return False
    return True


if __name__ == '__main__':
    p  = play()
    p.backTrack(10)
