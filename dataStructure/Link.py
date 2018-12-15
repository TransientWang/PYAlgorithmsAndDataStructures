# -*- coding: UTF-8 -*-
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from dataStructure import ListNode
from dataStructure import TreeNode


class sol(object):

    def sortedArrayToBST(self, nums):
        '''
        108.将有序数组转换为二叉搜索树
        思路：中间位置元素为树根
        :param nums:
        :return:
        '''
        mid = len(nums) // 2
        root = TreeNode.TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def addTwoNumbers(l1, l2):
        c = 0
        head = ListNode(0)
        node = head
        while l1 != None or l2 != None:
            t1, t2, sum = 0, 0, 0
            if l1 != None:
                t1 = l1.val
                l1 = l1.__next__
            if l2 != None:
                t2 = l2.val
                l2 = l2.__next__
            sum = t1 + t2 + c

            if sum < 10:
                node.val = sum
                c = 0
            else:
                c = 1
                node.val = abs(10 - sum)

            if l1 != None or l2 != None:
                node.next = ListNode(0)
                node = node.__next__
            elif c == 1:
                node.next = ListNode(1)
                node = node.__next__

        return head


def oddEvenList(head):
    '''
    奇偶链表
    思路：两个指针  一个指向奇节点 另一个指向偶数节点
    将偶数节点后面的节点 移动到 奇节点的后面 此时前面有两个奇数几点，后面是两个偶数节点
    重复次过程
    '''
    if not head:
        return None
    pre = head
    cur = head.next
    while cur and cur.next:
        tmp = pre.next  # 保存奇节点 后一个节点
        pre.next = cur.next  # 将奇节点的下一个偶节点的下一个
        cur.next = cur.next.next  # 偶节点的指向偶节点的后面第二个
        pre.next.next = tmp  # 将移动过来的奇节点的下一个指向之前的偶数节点
        pre = pre.next
        cur = cur.next
    return head


'''
相交链表
'''


def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = headB if p1 == None else p1.next
        p2 = headA if p2 == None else p2.next
    return p1
    # a = {}
    # while headA:
    #     a[headA] = 0
    #     headA = headA.next
    # while headB:
    #     if a.get(headB) !=None:
    #         return headB
    #     headB = headB.next
    # return None


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    # head.next = ListNode.ListNode(2)
    # head.next.next = ListNode.ListNode(3)
    # head.next.next.next = ListNode.ListNode(4)
    print(getIntersectionNode(head, head))
    # while h:
    #     print(h.val)
    #     h = h.next
