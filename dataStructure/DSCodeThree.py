# -*- coding: UTF-8 -*-
from dataStructure import ListNode


def longestValidParentheses(s):
    """
    TODO 可以优化，合并两次循环，判断合法的同时判断最优值
    32. 最长有效括号
    思路：用一个栈 保存索引，遇到匹配的弹出
    然后遍历栈，找出间距最大的值
    :param s:
    :return:
    """
    stack = []
    for i in range(len(s)):
        if s[i] == ')':
            if stack and s[stack[-1]] == '(':  ## 这里要注意，不能想当然地用s[i-1]，因为我们有些下标直接continue了没有存到栈中去
                stack.pop()
                continue
        stack.append(i)

    max_length = 0
    next_index = len(s)
    while stack:
        cur_idx = stack.pop()
        cur_length = next_index - cur_idx - 1
        max_length = max(max_length, cur_length)
        next_index = cur_idx
    return max(next_index, max_length)


def rotateRight(head, k):
    """
    61. 旋转链表
    思路：快慢指针，先测量长度
    然后找到移动节点（倒数第k），将链表末尾当做链表头
    移动节点当做链表末尾。
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    # ↓ 条件过滤
    if head is None:
        return []
    if head.next is None or k == 0:
        return head
    elif head.next.next is None:
        if k % 2 == 0:
            return head
        else:
            aft = head.next
            aft.next = head
            head.next = None
            return aft

    # ↓ 计算长度
    low, fast, lens, low_lens = head, head.next.next, 3, 1
    while fast.next and fast.next.next:
        low = low.next
        low_lens += 1
        fast = fast.next.next
        lens += 2
    if fast.next:
        fast = fast.next
        lens += 1
    # ↓ 寻找节点
    cur = None
    k %= lens
    # ↓ 优化如果条件适合可以从慢指针开始遍历
    if k % lens < lens - low_lens:
        cur = low
        for i in range(low_lens, lens - k):
            cur = cur.next
    else:
        cur = head
        for i in range(1, lens - k):
            cur = cur.next
    # ↓ 颠倒指针
    # head = cur.next
    # cur.next = None
    # fast.next = head
    # return head
    t = head
    # t, cur = head, head
    # for i in range(1, lens - k):
    #     cur = cur.next

    if not cur.next:
        return head
    head = cur.next
    cur.next = None
    fast.next = t
    return head


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    # head.next.next.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)
    print(rotateRight(head, 3))
