# -*- coding: UTF-8 -*-
from dataStructure import ListNode


def mergeKLists(lists):
    '''
    23.合并K个元素的有序链表
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
            L = len(lists) - 1
            i = 0
            while i <= L:
                if lists[i] is not None:
                    if lists[i].val <= h:
                        h = lists[i].val
                        m = i
                    i += 1
                else:
                    lists.remove(None)
                    L -= 1
            if m != -1:
                t.next = ListNode.ListNode(lists[m].val)
                t = t.next
                lists[m] = lists[m].next
        else:
            break
    return root.next


def mergeKListsOne(lists):
    '''
    23.合并K个元素的有序链表
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
    148.链表排序
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
    合并排序
    重点在于 没法设置合并的边界
    所以在找到中点的时候就要把原链表从中点断开

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
    '''
    快慢指针进行查找链表中点
    :param node:
    :return:
    '''
    slow = node
    fast = node.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def merge(left, right):
    '''
    合并
    :param left:
    :param right:
    :return:
    '''
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


import copy


def lowestCommonAncestor(root, p, q):
    """
    236.二叉树的最近公共祖先（review）
    思路：
    如果根节点为None，或者跟节点== q | p
    则可以直接返回
    如果不相等
    则寻找左孩子，右孩子
    如果左孩子右孩子返回的不等于空那么一定p或q或空
    如过都不为空，根节点就是最近公共祖先
    如果有一个为空，则继续递的找
     :type root: TreeNode
     :type p: TreeNode
     :type q: TreeNode
     :rtype: TreeNode
     """
    if not root or root.val == p.val or root.val == q.val:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left if left else right


def lowestCommonAncestor(root, p, q):
    """
            :type root: TreeNode
            :type p: TreeNode
            :type q: TreeNode
            :rtype: TreeNode
            """

    def isParent(p, node):
        if not p:
            return False
        if p == node:
            return True
        return isParent(p.left, node) or isParent(p.right, node)

    if root in [None, p, q]:
        return root
    if isParent(p, q):
        return p
    if isParent(q, p):
        return q
    while root:
        if isParent(root.left, p) and isParent(root.left, q):
            root = root.left
        elif isParent(root.right, p) and isParent(root.right, q):
            root = root.right
        else:
            return root
    return None


if __name__ == '__main__':
    from dataStructure import TreeNode

    root = TreeNode.TreeNode(3)

    root.left = TreeNode.TreeNode(5)
    root.right = TreeNode.TreeNode(1)

    root.left.left = TreeNode.TreeNode(6)
    root.left.right = TreeNode.TreeNode(2)

    root.left.right.left = TreeNode.TreeNode(7)
    root.left.right.right = TreeNode.TreeNode(4)

    root.right.left = TreeNode.TreeNode(0)
    root.right.right = TreeNode.TreeNode(8)
    print(lowestCommonAncestor(root, 5, 1).val)
