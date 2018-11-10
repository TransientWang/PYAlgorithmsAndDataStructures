# -*- coding: UTF-8 -*-


from dataStructure import ListNode

'''
删除链表中的节点
由于只有下一个节点 不能获取到上一节点
解决办法是 将下一节点的值 赋值给当前被删除节点，然后删除下一节点
'''


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.__next__


'''
删除链表的倒数第N个节点
双指针aft先往后走N，然后cur与aft一起走
当aft走到末尾时候 通过cur删除下一节点
特殊情情况是删除第一个节点的时候
'''


def removeNthFromEnd(head, n):
    cur = head
    aft = cur
    k = 1
    if head.__next__ == None:
        return None
    while aft.__next__ != None and k <= n:
        aft = aft.__next__
        k += 1
    if aft.__next__ == None and k <= n:  # 当删除正数第一个情况
        return head.__next__
    while aft.__next__ != None:
        cur = cur.__next__
        aft = aft.__next__

    if cur.__next__ != None:
        if cur.next.__next__ == None:
            cur.next = None
        else:
            cur.next = cur.next.__next__
    return head


'''
反转链表
'''


def reverseList(head):
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


'''
反转链表 这个方法很神奇
将当前的下一个赋值给下次循环的当前值，根据传入头找到链表的尾
'''


def reverseListOne(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre

'''
反转链表 递归
先直接走到倒数第二个一个节点，
然后逆置倒数第一个节点，返回递归
'''
def reverseListTwo(head):
    if head.__next__ == None:
        return head              #尾节点返回
    new_head = reverseListTwo(head.__next__) #当最后一次返回的时候new_head 为倒数第一个节点
    head.next.next = head     #第一次返回后处理的节点head 此时还是倒数第二个，这样就可以将最后两个逆置了
    head.next = None          #返回的new_head注意在if中是head,next也就是5，所以上一行代表吧new_head,next 5 指向 head 4
                                #然后将 new_head返回递归调用
    return new_head


'''
链表合并
'''


def mergeTwoLists(l1, l2):
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


'''
判断回文链表
要求时间复杂度O（n）空间复杂度为O（1）
思路：
先遍历一遍求出长度，然后直接逆置链表到一半的长度，（如果长度是奇数的话，忽略中间值）
然后向两头遍历，遇到不相等的就说明不是回文
'''


def isPalindrome(head):
    if head is None:
        return True
    length = 0
    tmp = head  # type: ListNode 遍历链表长度的临时变量
    while tmp is not None:
        length += 1
        tmp = tmp.__next__
    mid = length / 2 - 1  # type: Union[int, Any] 中间位置
    t = 0  # type: int 临时变量，帮助逆置链表到中间位置
    del tmp
    '''逆置链表'''
    cur, pre = head, None
    while cur and t <= mid:
        cur.next, pre, cur = pre, cur, cur.next
        t += 1
    del head, mid, t

    if length % 2 != 0: #如果长度是奇数，则忽略中位数
        cur = cur.__next__

    while pre is not None and cur is not None: #开始判断回文
        if pre.val == cur.val:
            pre = pre.__next__
            cur = cur.__next__
        else:
            return False
    return True


'''
链表有环
'''


def hasCycle(head):
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


'''
链表有环
快慢指针 两指针相遇的时候 就证明链表有环
'''


def hasCycleOne(head):
    if head is None or head.__next__ is None:
        return False
    slow, fast = head, head.next.__next__

    while slow != fast:
        if fast is None or fast.__next__ is None:
            return False
        slow = slow.__next__
        fast = fast.next.__next__
    return True


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)

    # end = ListNode.ListNode(2)
    # end.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)
    c = reverseListTwo(head)
    print(c)
    # while c.next != None:
    #     print(c.val)
    #     c = c.next
    # print(c.val)
