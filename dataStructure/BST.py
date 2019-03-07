# -*- coding: UTF-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.root = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        二叉搜索树查找
        """
        if not root:
            return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        二叉搜索树插入
        :param self:
        :param root:
        :param val:
        :return:
        """
        if val == root.val:
            return
        if val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        elif val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        self.root = root
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        平衡二叉树删除节点
        :param root:
        :param key:
        :return:
        """
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:  # 没有根节点直接删除
                return None
            elif root.left and not root.right:  # 只有一个节点
                return root.left
            elif root.right and not root.left:
                return root.right
            else:  # 两个子节点都有的情况下，找到中序遍历的前驱或者后继其中一个节点 t，将 t 替换为删除节点
                tr = self.searchMin(root.right)
                tr.left = root.left
                if root.right.val != tr.val:
                    tr.right = root.right
                return tr
        elif key > root.val:
            r = self.deleteNode(root.right, key)
            root.right = r
        else:
            l = self.deleteNode(root.left, key)
            root.left = l
        return root

    def searchMin(self, root):
        """
        找到二叉搜索树种最小的节点时
        按中序遍历后继，就是最左下的子树
        :param root:
        :return:
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
        p = stack.pop()
        if stack:  # 处理最左下子树的右子树
            stack[-1].left = p.right
            p.right = None
        return p

    def getIntervals(self):
        """
        352. 将数据流变为多个不相交间隔
        :rtype: List[Interval]
        """
        res = []
        root = self.root
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if res and root.val == res[-1][-1] + 1:
                    res[-1] = [res[-1][0], root.val]
                else:
                    res.append([root.val, root.val])

                root = root.right
        return res


if __name__ == '__main__':
    t = TreeNode(1)

    s = Solution()
    s.insertIntoBST(t, 1)
    s.insertIntoBST(t, 3)
    s.insertIntoBST(t, 7)
    s.insertIntoBST(t, 2)
    t = s.insertIntoBST(t, 6)

    print(s.getIntervals())
