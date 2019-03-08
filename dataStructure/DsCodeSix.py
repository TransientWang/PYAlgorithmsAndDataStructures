# -*- coding: UTF-8 -*-
from dataStructure import TreeNode
import os
import heapq


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
    331. 验证二叉树的前序序列化（review）
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
    337. 打家劫舍 III（review）
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


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
        return False
    t = [2 ** 31]
    for i in range(len(nums)):
        if len(t) > 2:
            return True
        else:
            if nums[i] > t[-1]:
                t.append(nums[i])
            else:
                b = False
                for j in range(len(t) - 1, -1, -1):
                    if nums[i] > t[j]:
                        b = True
                        t[j + 1] = nums[i]
                if not b:
                    t[0] = nums[i]

    return False


def kSmallestPairs(nums1, nums2, k):
    """
    373. 查找和最小的K对数字
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    if nums1 and nums2:
        n1, n2 = len(nums1), len(nums2)
        heap = [[nums1[0] + nums2[i], 0, i] for i in range(n2)]
        while k and heap:
            val, left, right = heapq.heappop(heap)
            res.append([nums1[left], nums2[right]])
            if left + 1 < n1:
                heapq.heappush(heap, [nums1[left + 1] + nums2[right], left + 1, right])
            k -= 1
    return res


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    root.right = TreeNode.TreeNode(3)
    root.left.right = TreeNode.TreeNode(5)
    print(increasingTriplet([2, 1, 5, 0, 4, 6]))
    # root.right.right = TreeNode.TreeNode(5)
