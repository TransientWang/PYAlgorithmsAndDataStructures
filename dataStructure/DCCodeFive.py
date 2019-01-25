# -*- coding: UTF-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val)


def connect(root):
    """
    117. 填充同一层的兄弟节点 II
    :param root: TreeLinkNode
    :return: Nothing
    """
    if not root:
        return root
    queue = [root]
    while queue:
        m = len(queue)
        tmp = None
        for i in range(m):
            t = queue.pop(0)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
            if not tmp:
                tmp = t
            else:
                tmp.next = t
                tmp = t


if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)
    connect(root)
