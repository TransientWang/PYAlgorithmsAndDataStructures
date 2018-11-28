# -*- coding: UTF-8 -*-
from dataStructure import ListNode


def mergeKLists(lists):
    '''
    合并K个元素的有序链表
    超时
    n:lists长度
    m:单个链表长度
    时间复杂度O（n) = (n*m)
    :param lists:
    :return:
    '''
    root = ListNode.ListNode(0)
    t = root
    while True:
        if len(lists) > 0:
            m = -1
            h = 2 ** 31
            l = len(lists) - 1
            i = 0
            while i <= l:
                if lists[i] is not None:
                    if lists[i].val <= h:
                        h = lists[i].val
                        m = i
                    i += 1
                else:
                    lists.remove(None)
                    l -= 1
            if m != -1:
                t.next = ListNode.ListNode(lists[m].val)
                t = t.next
                lists[m] = lists[m].next
        else:
            break
    return root.next


if __name__ == '__main__':
    r1 = ListNode.ListNode(1)
    r1.next = ListNode.ListNode(4)
    r1.next.next = ListNode.ListNode(5)

    r2 = ListNode.ListNode(1)
    r2.next = ListNode.ListNode(3)
    r2.next.next = ListNode.ListNode(4)

    r3 = ListNode.ListNode(2)
    r3.next = ListNode.ListNode(6)

    root = mergeKLists([r1, r2, r3])
    while root is not None:
        print(root.val, end=" ")
        root = root.next
