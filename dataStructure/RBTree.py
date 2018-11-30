# -*- coding: UTF-8 -*-
class RBTree(object):
    def __init__(self, val, color="r"):
        '''
        红黑树
        基本特征：
        1、节点是红色或者黑色
        2、根节点是黑色
        3、每个叶子节点（NIL）都是黑色
        4、红色节点的两个子节点都是黑色
        5、从任意节点到其每个叶子节点的路径上都包含相同数量的黑色节点

        :param val: 节点值
        :param color: 节点颜色
        '''
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def isBlackNode(self):
        return self.color == "b"

    def setBlackNode(self):
        self.color = "b"

    def setRedNode(self):
        self.color = "r"

    def printf(self):

        print(str(self.val)+self.color, end=" ")
        if self.left:
            self.left.printf()
        if self.right:
            self.right.printf()

    def left_rotate(self, node):
        '''
        节点左旋
          parent                      parent
        /                           /
    node              ->          right
  /    \                         /    \
ln      right                  node    ry
       /    \                 /   \
    ly       ry              ln   ly

        需要在注意的地方就是，一个需要有一个子节点和一个父节点需要处理。
        而要处理的节点有三个因为ly没有保存所以先处理ly
        然后node rNode ，因为已经保存了引用，所以顺序可以随意处理
        :param node:
        :return:
        '''
        pNode = node.parent
        rNode = node.right

        # 处理ly
        node.right = rNode.left  # node.right -> ly
        if node.right:
            node.right.parent = node  # ly.parent -> node

        # 处理node

        rNode.left = node  # rNode.left -> node
        node.parent = rNode  # node.parent -> rNode

        ##处理rNode

        rNode.parent = pNode
        if pNode:
            pNode.left = rNode

    def right_rotate(self, node):
        '''
        右旋：左旋的反过来就是右旋
        :param node:
        :return:
        '''
        pNode = node.parent
        lNode = node.left

        # 处理ly
        node.left = lNode.right  # node.right -> ly
        if node.left:
            node.left.parent = node  # ly.parent -> node

        # 处理node
        lNode.right = node  # rNode.left -> node
        node.parent = lNode  # node.parent -> rNode

        ##处理lNode

        lNode.parent = pNode
        if pNode:
            pNode.right = lNode

    def insert(self, node):
        pass


if __name__ == '__main__':
    root = RBTree(1)
    root.setBlackNode()
    root.left = RBTree(3)
    root.left.parent = root
    root.left.left = RBTree(2)
    root.left.left.setBlackNode()
    root.left.left.parent = root.left
    root.left.right = RBTree(5)
    root.left.right.parent = root.left
    root.left.right.setBlackNode()
    root.left.right.left = RBTree(4)
    root.left.right.left.parent = root.left.right
    root.left.right.right = RBTree(6)
    root.left.right.right.parent = root.left.right
    root.printf()
    print("\n")
    root.left_rotate(root.left)
    root.printf()
