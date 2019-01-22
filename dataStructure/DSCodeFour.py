# -*- coding: UTF-8 -*-
from dataStructure import ListNode
from dataStructure import TreeNode


def reverseBetween(head, m, n):
    """
    92. 反转链表 II
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if not head or m == n:
        return head
    pre = dummy = ListNode.ListNode(-1)
    dummy.next = head
    for i in range(m - 1):
        pre = pre.next

    cur = pre.next
    tail = cur
    pre.next = None
    tmp = pre
    pre = None

    for i in range(n - m + 1):
        cur.next, pre, cur = pre, cur, cur.next
    tmp.next = pre
    tail.next = cur
    return dummy.next


def generateTrees(n):
    """
    95. 不同的二叉搜索树 II
    递归
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return []

    def find(left, right):
        tmp = []

        if left > right:
            tmp.append(None)
            return tmp

        for i in range(left, right + 1):
            left_tree = find(left, i - 1)
            right_tree = find(i + 1, right)

            for lt in left_tree:
                for rt in right_tree:
                    node = TreeNode.TreeNode(i)
                    node.left = lt
                    node.right = rt
                    tmp.append(node)

        return tmp

    return find(1, n)




if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    mid = head.next.next.next.next
    mid.next = ListNode.ListNode(6)

    print(reverseBetween(head, 2, 4))
