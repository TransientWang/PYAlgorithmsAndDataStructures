# -*- coding: UTF-8 -*-
from dataStructure import ListNode


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


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    mid = head.next.next.next.next
    mid.next = ListNode.ListNode(6)

    print(reverseBetween(head, 2, 4))
