# -*- coding: UTF-8 -*-
class BSTIterator(object):

    def __init__(self, root):
        """
        173. 二叉搜索树迭代器
        中序遍历迭代版本
        :type root: TreeNode
        """
        self.stack = []
        self.cur = root

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.cur:  # 先将 left 节点全部添加进stack
            self.stack.append(self.cur)
            self.cur = self.cur.left
        if self.stack:
            cur = self.stack.pop()  # 开始处理最左边的叶子节点为当前节点
            p = cur.val
            self.cur = cur.right  # 将最左边节点的右节点当做当前节点。
            return p

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.cur or self.stack else False
