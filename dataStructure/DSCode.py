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


if __name__ == '__main__':
    r1 = ListNode.ListNode(-8)
    r1.next = ListNode.ListNode(-6)
    r1.next.next = ListNode.ListNode(-5)

    r2 = ListNode.ListNode(-8)
    r2.next = ListNode.ListNode(-6)
    r2.next.next = ListNode.ListNode(-6)

    r3 = ListNode.ListNode(-8)
    r3.next = ListNode.ListNode(-7)

    root = mergeKListsOne([r1, r2, r3])
    while root is not None:
        print(root.val, end=" ")
        root = root.next
