# -*- coding: UTF-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val)


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        st = str(self.label)
        for i in self.neighbors:
            st += str(i.x)
        print(st)
        return str(self.label)


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


def cloneGraph(node=UndirectedGraphNode(2)):
    """
    133. 克隆图
    :param node:a undirected graph node
    :return:a undirected graph node
    """
    if not node:
        return
    visited = {}

    def dfs(node):
        if node.label in visited:
            return visited[node.label]
        new_node = UndirectedGraphNode(node.label)
        visited[new_node.label] = new_node
        new_node.neighbors = [dfs(i) for i in node.neighbors]
        return new_node

    return dfs(node)


def detectCycle(head):
    """
    142. 环形链表 II
    链表只有环的情况下，两指针相遇的点为起点，
    当环外还有一定长度的链表的时候，相遇点距离起点的位移就是链表的长度
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    low, fast = head, head

    while fast and fast.next:  # 快慢指针条件
        low = low.next
        fast = fast.next.next
        if low == fast:
            fast = head
            while low != fast:
                low = low.next
                fast = fast.next
            return fast
    return None


def reorderList(head):
    """
    143. 重排链表
    思路：链表问题除了快慢指针，增加辅助节点以外，还可以与栈等数据结构集合使用
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    stack = []
    low, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        low = low.next
    low.next, low = None, low.next
    while low:
        stack.append(low)
        low = low.next
    while stack:
        fast = head.next
        head.next = stack.pop()
        head.next.next = fast
        head = fast


def preorderTraversal(root):
    """
    144. 二叉树的前序遍历
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    #递归
    # lists = [root.val]
    # lefts = preorderTraversal(root.left)
    # rights = preorderTraversal(root.right)
    # return lists + lefts + rights
    stack = []
    # 迭代
    lists = []
    stack = [root]
    while stack:
        p = stack.pop()
        lists.append(p.val)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)
    return lists


if __name__ == '__main__':
    from dataStructure import ListNode

    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    # root.left.left = TreeLinkNode(4)
    # root.left.right = TreeLinkNode(5)
    # root.right.right = TreeLinkNode(7)
    # connect(root)

    # node = UndirectedGraphNode(0)
    # nNode = UndirectedGraphNode(1)
    # pNode = UndirectedGraphNode(2)
    # node.neighbors = [nNode, pNode]
    # nNode.neighbors = [pNode]
    # pNode.neighbors = [pNode]
    # cloneGraph(node)
    head = ListNode.ListNode(1)
    head.next = ListNode.ListNode(2)
    head.next.next = ListNode.ListNode(3)
    head.next.next.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)
    print(preorderTraversal(root))
