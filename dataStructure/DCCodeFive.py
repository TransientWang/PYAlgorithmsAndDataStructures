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




if __name__ == '__main__':
    # root = TreeLinkNode(1)
    # root.left = TreeLinkNode(2)
    # root.right = TreeLinkNode(3)
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
    print(canCompleteCircuit([5,1,2,3,4],
[4,4,1,5,1]))
