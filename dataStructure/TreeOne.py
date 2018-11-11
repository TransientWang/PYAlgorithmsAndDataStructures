# -*- coding: UTF-8 -*-
'''
给定一个二叉树，返回它的中序 遍历。
'''

from dataStructure import TreeNode
def inorderTraversal(root):
    l = []
    find(root,l)
    return l

def find(root, l):
    if not root:
        return
    if root.left!=None:
        find(root.left, l)
    l.append(root.val)
    if root.right!=None:
        find(root.right, l)


if __name__ == '__main__':
        t = TreeNode.TreeNode(1)
        t.right = TreeNode.TreeNode(2)
        t.right.left = TreeNode.TreeNode(3)
        print(inorderTraversal(t))
