# -*- coding: UTF-8 -*-


from dataStructure import ListNode


def deleteNode(node):
    '''
    删除链表中的节点
    由于只有下一个节点 不能获取到上一节点
    解决办法是 将下一节点的值 赋值给当前被删除节点，然后删除下一节点
    '''
    node.val = node.next.val
    node.next = node.next.__next__


def removeNthFromEnd(head, n):
    '''
    review
    19.删除链表的倒数第N个节
    双指针aft先往后走N，然后cur与aft一起走
    当aft走到末尾时候 通过cur删除下一节点
    特殊情情况是删除第一个节点的时候
    思路:遍历链表用指针，要求遍历一遍，一个显然不够，那就再加一个。
    第一个原地，第二个后移n位，再同时后移。这样第二个遍历到末尾的时候，第一个正好再倒数第N的位置
    注意链表长度比N小的情况
    '''
    if head.next is None:
        return None
    first = head
    second = first
    i = 0
    while second.next != None and i < n:
        second = second.next
        i += 1
    while second.next != None:
        first = first.next
        second = second.next
    if first.next != None:
        if first.next.next != None:
            first.next = first.next.next
        else:
            first.next = None

    return head


def reverseList(head):
    '''
    反转链表
    '''

    if head.__next__ == None:
        return head
    pre = head
    cur = head.__next__
    if cur.__next__ == None:
        cur.next = head
        head.next = None
        return cur
    aft = cur.__next__
    head.next = None

    while cur.__next__ != None:
        cur.next = pre
        pre = cur
        cur = aft
        if cur.__next__ != None:
            aft = aft.__next__
    cur.next = pre
    return cur


def reverseListOne(head):
    '''
    206.反转链表 迭代（review）
    将当前的下一个赋值给下次循环的当前值，根据传入头找到链表的尾
    多重赋值，等号右边从左到右首先完成计算，然后等号左边从左到右边赋值
    将等号左右两边认为成元组，右边元组先完成计算，然赋值给左边元组等号一遍的顺序可以调换。
    '''
    cur, pre = head, None
    while cur:
        cur.next, cur, pre = pre, cur.next, cur  # 逻辑：cur.next->pre|cur游标后移一位|将cur赋值给pre
        # 首先等号右边的三个值已经被记录，也就是cur.next现在就是持有cur.next节点。
        # 赋值的时候 等号左边 第一个先赋值，此时cur.next 指向pre（此时为null）,然后第二个赋值，cur移动到了已经记录的cur.next
        # 位置（即使cur的下一个节点已经指向为null，但是由于cur.next提前记录好了所以赋值没有问题），最后是将pre移动到已经记录好的
        # cur原位置（右边cur的引用还指向原处，不会因为其他赋值语句而变化）
    return pre


def reverseListTwo(head):
    '''
    206.反转链表 递归（review）
    先直接走到倒数第二个节点，
    然后逆置倒数第一个节点，返回递归
    1 2 3 4 5 6
    1 2 3 4 6 -> 5 # 4.next 为 5
    1 2 3 6 -> 5 -> 4 #3.next 为 4
    '''
    if head.next == None:
        return head  # 尾节点返回
    new_head = reverseListTwo(head.next)  # 当最后一次返回的时候new_head 为倒数第一个节点
    head.next.next = head  # 第一次返回后处理的节点head 此时还是倒数第二个，这样就可以将最后两个逆置了
    head.next = None  # 逆置过后此时最后两个节点的next指针值互相指向对方，
    # 此时要把倒数第二个指向置null，然后将倒数第一个节点返回
    # 然后将 new_head返回递归调用
    return new_head


def mergeTwoLists(l1, l2):
    '''
    链表合并
    '''
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    head, cur = None, None

    if l1.val <= l2.val:
        head = l1
        l1 = l1.__next__
    else:
        head = l2
        l2 = l2.__next__
    cur = head
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.__next__
        else:
            cur.next = l2
            l2 = l2.__next__
        cur = cur.__next__
    while l1 != None:
        cur.next = l1
        l1 = l1.__next__
        cur = cur.__next__
    while l2 != None:
        cur.next = l2
        l2 = l2.__next__
        cur = cur.__next__
    return head


def isPalindrome(head):
    '''
	234.回文链表
	review
    思路：快慢指针
    快指针一次移动两位
    慢指针一次移动一位，这样快指针到末尾的时候满指针吗刚好到中间
    左边的每次反转，右边的继续遍历
    注意：奇数的时候需要忽略中间值。所以需要记录链表长度
    考察点：快慢指针
    :param head:
    :return:
    '''
    if head is None:
        return True
    left, cur, right = head, head, None
    i = 0  # 快慢指针辅助计数
    lens = 1  # 链表长度
    while cur.next != None:
        cur = cur.next
        i += 1
        lens += 1
        if i == 2:
            left.next, left, right = right, left.next, left  # 反转链表
            i = 0
    if i != 0:  # 偶数情况，还需要继续反转后移一位
        left.next, left, right = right, left.next, left
    if lens % 2 == 1:
        left = left.next

    while left != None and right != None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


def hasCycle(head):
    '''
    141.环形链表
    '''

    if head == None:
        return False
    dp = {}

    while head != None:
        if head in dp:
            return True
        else:
            dp[head] = 1
            head = head.__next__
    return False


def hasCycleOne(head):
    '''
    141.环形链表
    review
    快慢指针 两指针相遇的时候 就证明链表有环
    '''
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next

    return True


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)

    # end = ListNode.ListNode(2)
    # end.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)
    print(reverseListTwo(head))
    # print(c)
    # while c.next != None:
    #     print(c.val)
    #     c = c.next
    # print(c.val)
