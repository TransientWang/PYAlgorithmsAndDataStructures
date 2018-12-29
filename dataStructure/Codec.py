# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        297.二叉树的序列化与反序列化
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        queue = [root]
        ser = []
        while len(queue) != 0:
            tmp = queue.pop(0)
            if tmp:
                ser.append(tmp)
                queue.append(tmp.left)
                queue.append(tmp.right)
            else:
                ser.append(None)
        return ser

    def deserialize(self, data):
        """
        反序列化用一个queue保存构建的树
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        root = data.pop(0)

        stack = [root]

        while len(data) != 0:
            tmp = stack.pop(0)
            if len(data) > 0 and data[0] is None:
                data.pop(0)
            elif len(data) > 0:
                leftNode = data.pop(0)
                tmp.left = leftNode
                stack.append(leftNode)
            if len(data) > 0 and data[0] is None:
                data.pop(0)
            elif len(data) > 0:
                rightNode = data.pop(0)
                tmp.right = rightNode
                stack.append(rightNode)

        return root


def ladderLength(beginWord, endWord, wordList):
    '''
    127.单词接龙
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    求最短路径：考察知识点 BFS（广度优先遍历）
    思路：这道题beginWord可以不再字典中，但是endWord必须在字典中，
    首先，创建一个队列，保存我们遍历的记录，把beginWord入队，在将一个逗号“，”入队，证明这是第一层
    从beginWord开始变换，把它的每一位上的字符 都替换成 a-z 然后比较其是否在字典中，有的话说明它的其中一次变换
    可能是这个值，把它入队，然后继续指导beginWord所有字符都替换比较完一遍。
    说明beginWord的所有可能变换的字符串都已经找到，也代表这一层已经遍历完，此时队列中保存的是上一层的逗号”，”还有beginword的可能变换字符串
    可以再次从队列中弹出新的元素比较。这时候弹出来的是逗号“，”，证明刚才已经把上一层的元素都弹出来遍历的
    已经可以遍历下一层了，可以用一个变量times记录已经遍历过得层数，然后就要在将一个逗号作为当前层的标记入队，然后重新弹出一个新的元素。新弹出的元素按照之前的步骤
    直到再遇见逗号，代表又遍历完这一层 当遍历的字符串刚好是endword并且它在字典中的时候，我们就可以结束遍历，因为先遇到的
    一定是最短序列，由于结束时，我们这一层还没有遍历完，正常情况下要等到下一层的时候才能弹出上一层的逗号，并记录。
    还要入队当前层的逗号，所以，当结束的时候，还有两个逗号，代表两层没有记录在变量times中。所以返回times+2

    但是如果把队列中的元素都弹出来了，也没有遇见endWord说明 endWord不在字典中，也就不能转换成endWord，返回0

    :param beginWord:
    :param endWord:
    :param wordList:
    :return:
    '''
    if endWord not in wordList:
        return 0
    if beginWord in wordList:
        wordList.remove(beginWord)
    import string

    begin_set, end_set = {beginWord}, {endWord}
    word_list_set = set(wordList)

    step = 2  # 开始一层，结束一层没有计算
    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set  # 减少计算量
        tmp = set()
        for word in begin_set:  # 遍历每一层
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]  # 替换
                    if new_word in end_set:
                        return step
                    if new_word in word_list_set:
                        word_list_set.discard(new_word)  # 从单词集里删除已查找到单词
                        tmp.add(new_word)  # 找到的单词加入当前层
        begin_set = tmp  # 交给下一层
        step += 1
    return 0


def solve(board):
    '''
    考察点BFS
    130.被围绕的区域
    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
    思路：遍历周边区域就可以，遇到 O 就将 O 替换成 # 然后BFS
    最后将0替换成X 将#替换成 O
    :param board:
    :return:
    '''
    if len(board) == 0:
        return
    row = len(board)
    colum = len(board[0])

    def find(x, y):
        if (x >= 0 and x < row and y >= 0 and y < colum) and board[x][y] == "O":
            board[x][y] = "#"

            find(x + 1, y)
            find(x - 1, y)
            find(x, y + 1)
            find(x, y - 1)
            # board[x][y] = "O" # 不能有这一步,

    for i in range(row):
        if board[i][0] == "O":
            find(i, 0)
    for i in range(row):
        if board[i][colum - 1] == "O":
            find(i, colum - 1)
    for i in range(colum):
        if board[0][i] == "O":
            find(0, i)
    for i in range(colum):
        if board[row - 1][i] == "O":
            find(row - 1, i)

    for x in range(row):
        for y in range(colum):
            if board[x][y] == "O":
                board[x][y] = "X"
            elif board[x][y] == "#":
                board[x][y] = "O"

    for i in range(row):
        print(board[i])


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    root.right = TreeNode.TreeNode(3)
    root.right.left = TreeNode.TreeNode(4)
    root.right.right = TreeNode.TreeNode(5)
    codex = Codec()
    # p = codex.deserialize(codex.serialize(root))
    # print(p)

    print(solve([["O", "X", "O", "O", "O", "O", "O", "O", "O"],
                 ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
                 ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
                 ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
                 ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
                 ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
                 ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
                 ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
                 ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]))
