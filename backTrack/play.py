# -*- coding: UTF-8 -*-
import math

import copy


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
    给定一个没有重复数字的序列，返回其所有可能的全排列。
    '''
    import copy
    if not nums:
        return
    res = []
    if len(nums) == 0:
        return res
    if len(nums) == 0:
        return [nums]

    def backTrack(before, nums):
        now = copy.deepcopy(before)
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
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        num = nums[i]
        sub = permuteOne(nums[:i] + nums[i + 1:])
        for j in sub:
            res.append([num] + j)
    return res


def subsets(nums):
    res = [[]]
    for i in range(len(nums)):
        sub = subsets(nums[i + 1:])
        for j in sub:
            t = [nums[i]] + j
            res.append(t)
    return res


def exist(board, word):
    '''
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


def findWords(board, words):
    '''
    单词搜索二
    这种方法会超时
    正确解法是 前缀树 + DFS
    :param board:
    :param words:
    :return:
    '''
    row = len(board[0]) - 1
    colum = len(board) - 1
    first = [words[i][0] for i in range(len(words))]

    def find(word, x, y, p, l):

        if x < 0 or x > colum or y < 0 or y > row or board[x][y] == "0":
            return False
        word += board[x][y]
        if len(word) != 0 and word[-1] != p[l]:
            return False
        elif str(word) == p:
            return True

        t = board[x][y]
        board[x][y] = "0"
        bool = find(word, x + 1, y, p, l + 1) or find(word, x, y + 1, p, l + 1) or \
               find(word, x - 1, y, p, l + 1) or find(word, x, y - 1, p, l + 1)
        board[x][y] = t
        return bool

    res = []
    for x in range(colum + 1):
        for y in range(row + 1):
            if board[x][y] in first:
                k = []
                for i in range(len(first)):
                    if first[i] == board[x][y]:
                        k.append(i)
                for i in k:
                    if find("", x, y, words[i], 0):
                        first[first.index(board[x][y])] = "-1"
                        res.append(words[i])

    return list(set(res))


def findWordsOne(board: list, words: list):
    row = len(board) - 1
    colum = len(board[0]) - 1
    from dataStructure import TrieNode
    res = []

    def find(x: int, y: int, p, curNode: TrieNode.Trie):

        p += board[x][y]
        if curNode.get("#") is not None and curNode["#"] is True:
            res.append(p[:len(p)])
        t = board[x][y]
        board[x][y] = "-1"
        if x + 1 <= row and board[x + 1][y] in curNode:
            find(x + 1, y, p, curNode[board[x + 1][y]])
        if x - 1 >= 0 and board[x - 1][y] in curNode:
            find(x - 1, y, p, curNode[board[x - 1][y]])
        if y + 1 <= colum and board[x][y + 1] in curNode:
            find(x, y + 1, p, curNode[board[x][y + 1]])
        if y - 1 >= 0 and board[x][y - 1] in curNode:
            find(x, y - 1, p, curNode[board[x][y - 1]])
        board[x][y] = t

    node = TrieNode.Trie()
    for i in words:
        node.insert(i)
    for x in range(row + 1):
        for y in range(colum + 1):
            if board[x][y] in node.root:
                find(x, y, "", node.root[board[x][y]])

    return list(set(res))


def isMatch(s, p):
    """
    TODO 好好看看
    通配符
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
        if p_index < len_p and p[p_index] == "*":
            p_start = p_index
            p_index += 1
            s_start = s_index
        elif p_index < len_p and (p[p_index] == "?" or p[p_index] == s[s_index]):
            p_index += 1
            s_index += 1
        elif p_start > -1:  # 如果p_index>0说明曾经碰见过 *，而且p[p_index]现在是*后面的第一个字母但是与是不匹配
            s_start += 1  # ，因为*可以匹配任意的字符串 ，而且当前的字符并不匹配P串后面的字符，所以将S串要开始的索引后移一位
            s_index = s_start
            p_index = p_start
        else:
            return False
    for i in range(p_index, len_p):
        if p[i] != "*":
            return False
    return True


if __name__ == '__main__':
    print(isMatch("aad", "*d"))
