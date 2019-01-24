# -*- coding: UTF-8 -*-
from dataStructure import TreeNode
from dataStructure import ListNode


def sortedListToBST(head):
    """
    109. 有序链表转换二叉搜索树
    思路：遍历求长度，递归创建树
    :type head: ListNode
    :rtype: TreeNode
    """

    def create(tmp, l, r):
        if l > r:
            return None
        mid = (l + r) // 2  # 因为已经有序，平衡二叉树选取列表中点作为根节点就可以
        root = TreeNode.TreeNode(tmp[mid])
        root.left = create(tmp, l, mid - 1)
        root.right = create(tmp, mid + 1, r)
        return root

    p = head
    tmp = []
    while p:
        tmp.append(p.val)
        p = p.next

    return create(tmp, 0, len(tmp) - 1)


def isBalanced(root):
    """
    110. 平衡二叉树
    递归解决 -1 代表不是平衡二叉树
    :type root: TreeNode
    :rtype: bool
    """

    def find(root):
        if not root:
            return 0
        left = find(root.left)
        right = find(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + left if left > right else 1 + right

    if find(root) == -1:
        return False
    return True


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    mid = head.next.next.next.next
    mid.next = ListNode.ListNode(6)

    root = TreeNode.TreeNode(3)
    root.left = TreeNode.TreeNode(9)
    root.right = TreeNode.TreeNode(20)
    root.right.left = TreeNode.TreeNode(15)
    root.right.right = TreeNode.TreeNode(7)
    isBalanced(root)
