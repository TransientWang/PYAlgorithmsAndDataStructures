# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        res = []
        queue = []
        queue.append(root)

        while len(queue) != 0:
            tmp = queue.pop(0)
            if not tmp is None:
                res.append(tmp.val)

                if tmp.left is None:
                    queue.append(None)
                else:
                    queue.append(tmp.left)
                    # res.append(tmp.left.val)
                if tmp.right is None:
                    queue.append(None)
                else:
                    queue.append(tmp.right)
                    # res.append(tmp.right.val)

            else:
                res.append(None)
        while res[-1] is None:
            res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        stack = []
        root = TreeNode.TreeNode(data.pop(0))
        stack.append(root)
        while len(data) != 0:
            tmp = stack.pop(0)
            if len(data) > 0:

                if len(data) > 0 and data[0] is None:
                    data.pop(0)
                elif len(data) > 0:
                    leftNode = TreeNode.TreeNode(data.pop(0))
                    tmp.left = leftNode
                    stack.append(leftNode)
                if len(data) > 0 and data[0] is None:
                    data.pop(0)
                elif len(data) > 0:
                    rightNode = TreeNode.TreeNode(data.pop(0))
                    tmp.right = rightNode
                    stack.append(rightNode)

        return root


def ladderLength(beginWord, endWord, wordList):
    '''
    单词接龙
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
    import string
    dmap = set(wordList)
    queue = [beginWord]
    queue.insert(0, ",")
    time = 2
    while len(queue) != 0:
        s = queue.pop()
        if s != ",":
            for i in range(len(s)):
                for k in string.ascii_lowercase:
                    t = s[:i] + k + s[i + 1:]
                    if t in dmap:
                        queue.insert(0, t)
                        dmap.discard(t)
                        if t == endWord:
                            return time
        elif len(queue) != 0:
            queue.insert(0, ",")
            time += 1
    return 0


def ladderLengthOne(beginWord, endWord, wordList):
    '''
    单词接龙
    最快的解法
    :param beginWord:
    :param endWord:
    :param wordList:
    :return:
    '''
    import string
    begin_set, end_set = {beginWord}, {endWord}
    word_list_set = set(wordList)
    size = len(beginWord)
    step = 2

    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        tmp = set()
        for word in begin_set:
            for i in range(size):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in end_set:
                        return step
                    if new_word in word_list_set:
                        word_list_set.discard(new_word)

                        tmp.add(new_word)
        begin_set = tmp
        step += 1
    return 0


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    # root.right = TreeNode.TreeNode(3)
    # root.right.left = TreeNode.TreeNode(4)
    # root.right.right = TreeNode.TreeNode(5)

    print(ladderLengthOne(beginWord="hit",
                          endWord="cog",
                          wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
