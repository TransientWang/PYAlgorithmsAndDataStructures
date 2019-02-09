# -*- coding: UTF-8 -*-
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