# -*- coding: UTF-8 -*-
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from dataStructure import ListNode
from dataStructure import TreeNode


class sol(object):


    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) / 2
        node = TreeNode.TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node

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
if __name__ == '__main__':
    sols = sol()
    node = sols.sortedArrayToBST([-10, -3, 0, 5, 9])
    print((node.val))
