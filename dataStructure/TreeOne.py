# -*- coding: UTF-8 -*-
'''
给定一个二叉树，返回它的中序 遍历。
'''

from dataStructure import TreeNode


def inorderTraversal(root):
    l = []
    find(root, l)
    return l


def find(root, l):
    if not root:
        return
    if root.left != None:
        find(root.left, l)
    l.append(root.val)
    if root.right != None:
        find(root.right, l)


'''
二叉树的锯齿形层次遍历
注意直接反转结果，不要在队列上反转
'''


def zigzagLevelOrder(root):
    stack = [root]
    k = 1
    result = []
    while len(stack) != 0:
        i = len(stack)
        r = []
        while i > 0:
            t = stack.pop(0)
            r.append(t.val)
            if t.left:
                stack.append(t.left)
            if t.right:
                stack.append(t.right)
            i -= 1
        if k % 2 == 0:
            r.reverse()
        k += 1
        result.append(r)
    return result


'''
从前序与中序遍历序列构造二叉树
思路：解决这个问题的是关键 是要明确二叉树的遍历是一个递归的过程
根据前序遍历 可以得到 根节点 
那么在 中序遍历中  可以根据前序遍历得到的根节点 获得到 根节点的左右子树信息
然后回到 前序遍历序列 中找到得到的左子树，那么在前序遍历中找到的左子树序列 也满足前序遍历序列
他的第一个索引 也一样是左子树的头结点  这就是一个递归的过程
'''


def buildTree(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    head = TreeNode.TreeNode(preorder[0])
    i = inorder.index(preorder[0])
    head.left = buildTree(preorder[1:i + 1], inorder[:i])
    head.right = buildTree(preorder[i + 1:], inorder[i + 1:])
    return head


'''
每个节点的右向指针
思路：此问题还是考察的二叉树层序遍历
只要在每层遍历的过程中保存先前节点 并将 先前节点的下一个指向当前节点
循环往复就可以
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if root is None:
        return None
    r = TreeLinkNode(1)
    mqueue = []

    mqueue.append(root)

    while len(mqueue) != 0:
        l = len(mqueue)
        tlNode = mqueue.pop(0)
        if tlNode.left is not None:
            mqueue.append(tlNode.left)
        if tlNode.right is not None:
            mqueue.append(tlNode.right)
        while l > 1:
            afNode = mqueue.pop(0)
            if afNode.left is not None:
                mqueue.append(afNode.left)
            if afNode.right is not None:
                mqueue.append(afNode.right)
            tlNode.next = afNode
            tlNode = afNode
            l -= 1
    return root


if __name__ == '__main__':
    # t = TreeNode.TreeNode(1)
    # t.right = TreeNode.TreeNode(2)
    # t.right.left = TreeNode.TreeNode(3)
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    head = connect(root)
    print(head.val)

    # head = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    # print(head.val)
