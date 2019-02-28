# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


def countNodes(root):
    """
    222. 完全二叉树的节点个数
    :type root: TreeNode
    :rtype: int
    """

    def getDepth(root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    if not root:
        return 0

    left_depth = getDepth(root.left)
    right_depth = getDepth(root.right)
    if left_depth == right_depth:
        return (1 << left_depth) + countNodes(root.right)  # 要算上根节点 1，所以将计算左子树个数 -1 抵消了
    return (1 << right_depth) + countNodes(root.left)
    # if not root:
    #   return 0
    # left = right = root
    # hight = 1
    # while not right:
    #     left = left.left
    #     right = right.right
    #     h += 1
    # if not left:
    #     return (1 << hight) - 1
    # return 1 + countNodes(root.left) + countNodes(root.right)


def invertTree(root):
    """
    226. 翻转二叉树
    同样的代码在 py和py3 中执行速度查太多了
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    left_ = root.left
    right_ = root.right
    invertTree(left_)
    invertTree(right_)
    root.right = left_
    root.left = right_
    return root


def binaryTreePaths(root):
    """
    257. 二叉树的所有路径
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []
    res = []

    def find(root=root, t=str(root.val)):
        if root.left:
            p = t + ("->" + str(root.left.val))
            find(root.left, p)
        if root.right:
            p = t + ("->" + str(root.right.val))
            find(root.right, p)
        if not root.left and not root.right:
            res.append(t)

    find()
    return res


def isValidSerialization(preorder):
    """
    331. 验证二叉树的前序序列化
    思路：二叉树叶子节点等于非叶子节点 + 1
    :type preorder: str
    :rtype: bool
    """
    res = 1
    for i in preorder.split(','):
        if not res:  # 不能有根是叶子
            return False
        if i == "#":
            res -= 1
        else:
            res += 1
    return not res


def rob(root: TreeNode) -> int:
    """
    337. 打家劫舍 III
    :param self:
    :param root:
    :return:
    """

    def dfs(root):
        if not root:
            return [0, 0]  # [抢劫了root,没有抢劫root]
        left = dfs(root.left)
        right = dfs(root.right)
        # 返回结果的第一个元素为我们抢劫了当前root,那么我们只能加上左右子树没有抢劫的值，
        # 第二个元素是我们不抢劫当前root,那么我们可以随意抢劫连个子树的任意组合。
        return [left[1] + right[1] + root.val, max(left) + max(right)]

    return max(dfs(root))


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    root.right = TreeNode.TreeNode(3)
    root.left.right = TreeNode.TreeNode(5)
    # root.right.right = TreeNode.TreeNode(5)
