# -*- coding: UTF-8 -*-
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(head):
    '''
    138.赋值随机指针
    :param head:
    :return:
    '''
    if not head:
        return None
    cur = head
    while cur:  # 复制一个新指针在原指针后面
        node = RandomListNode(cur.label)
        node.next = cur.next
        cur.next = node
        cur = node.next
    cur = head
    while cur:  # 复制随机指针
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur = head
    res = head.next
    while cur:  # 将原指针移除
        tmp = cur.next  # node
        cur.next = tmp.next
        if tmp.next:
            tmp.next = tmp.next.next
        cur = cur.next
    return res


def maxDepth(root):
    '''
    141.二叉树的最大深度
    :param self:
    :param root:
    :return:
    '''
    deepth = 1
    queue = [root]
    while len(queue) != 0:
        deepth += 1
        lens = len(queue)
        for i in range(lens):
            t = queue.pop(0)
            if t.left is not None:
                queue.append(t.left)
            if t.right is not None:
                queue.append(t.right)

    return deepth


def isValidBST(root):
    '''
    TODO 再看
    98.验证二叉搜索树
    思路：类似DFS,保存上一个节点的值作为最大值或者最小值，分别向两边搜索。
    :param root:
    :return:
    '''

    def validBST(self, root, small, large):
        if root == None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    return validBST(root, -2 ** 32, 2 ** 32 - 1)


def isSymmetric(root):
    '''
    101.对称二叉树
    递归
    :param root:
    :return:
    '''

    def isMirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root, root)


def isSymmetricOne(root):
    '''
    101.对称二叉树
    迭代
    :param root:
    :return:
    '''
    queue = [root, root]

    while len(queue) != 0:
        t1 = queue.pop(0)
        t2 = queue.pop(0)
        if t1.val == t2.val:
            return False
        if t1 is None or t2 is None:
            return False
        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)
    return True


def levelOrder(root):
    '''
    102.二叉树层次遍历
    :param root:
    :return:
    '''
    if not root:
        return []
    quque = [root]
    res = []
    while len(quque) != 0:
        lens = len(quque)
        t = []
        for i in range(lens):
            k = quque.pop(0)
            t.append(k.val)
            if k.left is not None:
                quque.append(k.left)
            if k.right is not None:
                quque.append(k.right)

        res.append(t)
    return res


from dataStructure import ListNode


def swapPairs(head):
    """
    24. 两两交换链表中的节点
    思路：1.在链表前面加一个辅助的虚拟节点
          2.使用递归
    :param head:
    :return:
    """
    # dummy = ListNode.ListNode(-1)
    # dummy.next = head
    # cur = dummy
    # while cur.next and cur.next.next:
    #     one, two, three = cur.next, cur.next.next, cur.next.next.next
    #     cur.next = two
    #     two.next = one
    #     one.next = three
    #     cur = one
    # return dummy.next

    if not head or not head.next:
        return head
    tmp = head.next
    head.next = swapPairs(head.next.next)
    tmp.next = head
    return tmp


def reverseKGroup(head, k):
    """
    25. k个一组翻转链表
    """
    if not head:
        return head
    cur, nextOne, pre, m = head, None, None, 0
    while m < k and cur:  # 正常逆置
        cur.next, cur, pre = pre, cur.next, cur
        m += 1
    if m < k:  # 当遍历到最后发现不够长，最后几个需要恢复逆置
        cur, pre = pre, None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        pre = head
    else:
        head.next = reverseKGroup(cur, k)
    return pre


if __name__ == '__main__':
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    head.next.next.next.next = ListNode.ListNode(5)
    p = reverseKGroup(head, 3)
    while p:
        print(p.val)
        p = p.next
