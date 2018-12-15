# -*- coding: UTF-8 -*-
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(head):
    '''
    赋值随机指针
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



if __name__ == '__main__':
    isValidBST(None)
