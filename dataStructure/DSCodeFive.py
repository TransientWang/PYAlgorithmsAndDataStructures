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


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    mid = head.next.next.next.next
    mid.next = ListNode.ListNode(6)
    sortedListToBST(head)
