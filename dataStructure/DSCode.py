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


def mergeKListsOne(lists):
    '''
    合并K个元素的有序链表
    其实考的是nlgn的排序算法，把链表里的数存在数组里堆排序
    或者快排
    然后在重新变成链表输出
    :param lists:
    :return:
    '''
    lis = []
    for i in lists:
        if i is not None:
            t = i
            while t is not None:
                lis.append(t.val)
                t = t.next
    buildMinHeap(lis)
    l = len(lis) - 1
    for i in range(1, len(lis) + 1):
        lis[0], lis[-i] = lis[-i], lis[0]
        heapAdjest(lis, 0, l)
        l -= 1

    root = ListNode.ListNode(0)
    t = root
    for i in range(1, len(lis) + 1):
        t.next = ListNode.ListNode(lis[-i])
        t = t.next
    return root.next


def buildMinHeap(list):
    for i in range(len(list) // 2 - 1, -1, -1):
        heapAdjest(list, i, len(list))


def heapAdjest(list, index, heapSize):
    left = index * 2 + 1
    right = index * 2 + 2
    if left < heapSize and list[index] > list[left]:
        list[left], list[index] = list[index], list[left]
        heapAdjest(list, left, heapSize)
    if right < heapSize and list[index] > list[right]:
        list[right], list[index] = list[index], list[right]
        heapAdjest(list, right, heapSize)


def sortList(head):
    '''
    链表排序
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
    :param head:
    :return:
    '''
    if head is None or head.next is None:
        return head
    left = head
    mid = getMid(head)
    right = mid.next
    mid.next = None
    left = sortList(left)
    right = sortList(right)
    return merge(left, right)


def getMid(node):
    slowNode = node
    fastNode = node.next
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    return slowNode


def merge(left, right):
    if not left:
        return right
    elif not right:
        return left
    res = ListNode.ListNode(0)
    cur = res

    while left is not None and right is not None:
        if left.val < right.val:
            cur.next = ListNode.ListNode(left.val)
            cur = cur.next
            left = left.next
        else:
            cur.next = ListNode.ListNode(right.val)
            cur = cur.next
            right = right.next
    while left:
        cur.next = ListNode.ListNode(left.val)
        cur = cur.next
        left = left.next
    while right:
        cur.next = ListNode.ListNode(right.val)
        cur = cur.next
        right = right.next

    return res.next


if __name__ == '__main__':
    r1 = ListNode.ListNode(3)
    r1.next = ListNode.ListNode(4)
    r1.next.next = ListNode.ListNode(1)

    r2 = ListNode.ListNode(-8)
    r2.next = ListNode.ListNode(-6)
    r2.next.next = ListNode.ListNode(-6)

    r3 = ListNode.ListNode(-8)
    r3.next = ListNode.ListNode(-7)

    root = sortList(r1)
    while root is not None:
        print(root.val, end=" ")
        root = root.next
