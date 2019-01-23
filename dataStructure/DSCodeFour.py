# -*- coding: UTF-8 -*-
from dataStructure import ListNode
from dataStructure import TreeNode


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


def generateTrees(n):
    """
    95. 不同的二叉搜索树 II
    递归
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return []

    def find(left, right):
        tmp = []

        if left > right:
            tmp.append(None)
            return tmp

        for i in range(left, right + 1):
            left_tree = find(left, i - 1)
            right_tree = find(i + 1, right)

            for lt in left_tree:
                for rt in right_tree:
                    node = TreeNode.TreeNode(i)
                    node.left = lt
                    node.right = rt
                    tmp.append(node)

        return tmp

    return find(1, n)


def recoverTree(root):
    """
    99. 恢复二叉搜索树
    先中序遍历，在与排序的列表比较，找出错误的一对
    然后再遍历序列然后交换
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    res = []

    def inorder(root):
        """
        中序遍历
        :param root:
        :return:
        """
        if not root:
            return []
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    def swap(root):
        """
        遍历并交换
        :param root:
        :return:
        """
        if not root:
            return
        swap(root.left)
        if root.val == diff[0]:
            root.val = diff[1]
        elif root.val == diff[1]:
            root.val == diff[0]
        swap(root.right)

    inorder(root)

    nodes = res[:]
    nodes.sort()
    diff = []

    for i in range(len(res)):
        if nodes[i] != res[i]:
            diff.append(nodes[i])

    swap(root)


def recoverTreeOne(root):
    """
    99. 恢复二叉搜索树
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    first, second, prev = None, None, None
    pred = None  # rightmost node in left tree

    cur = root
    while cur:
        # for each node, we compare it with prev node as we did in in-order-traversal
        if prev and cur.val < prev.val:
            if not first:
                first = prev
            # we may have corner case that two incorrect nodes are in same pair.
            # so we assign second with a new node at each time
            second = cur
        if cur.left:  # got left tree, then let's locate its rightmost node in left tree
            pred = cur.left
            # we may have visited the left tree before,
            # and connect the rightmost node with curr node (root node)
            while pred.right and pred.right != cur:
                pred = pred.right
            if pred.right == cur:  # this condition happens if and only if we have visited left tree before
                # if this left tree has been visited before, then we are done with it
                # cut the connection with currNode and start visit curr's right tree
                pred.right = None
                prev = cur
                cur = cur.right
            else:
                # if this left tree has not been visited before,
                # then we create a back edge from rightmost node to curr node,
                # so we can return to the start point after done the left tree
                pred.right = cur
                cur = cur.left
        else:  # no left tree, then just visit its right tree
            prev = cur
            cur = cur.right
    first.val, second.val = second.val, first.val


def levelOrderBottom(root):
    """
    107. 二叉树的层次遍历 II
    用栈存储每层的结果
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    queue = []
    queue.append(root)
    res = []
    while queue:
        lens = len(queue)
        t = []
        for i in range(lens):
            tmp = queue.pop(0)
            t.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        res.insert(0, t)
    return res


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    mid = head.next.next.next.next
    mid.next = ListNode.ListNode(6)

    print(reverseBetween(head, 2, 4))
