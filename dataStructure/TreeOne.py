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


if __name__ == '__main__':
    t = TreeNode.TreeNode(1)
    t.right = TreeNode.TreeNode(2)
    t.right.left = TreeNode.TreeNode(3)
    print(zigzagLevelOrder(t))
