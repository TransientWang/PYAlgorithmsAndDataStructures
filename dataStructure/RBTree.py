# -*- coding: UTF-8 -*-
class RBTree(object):
    '''
    红黑树（特殊的二叉查找树）
    基本特征：
    1.节点不是红色就是黑色
    2.根节点和叶子节点是黑色（叶子节点为 NIL或者空节点）
    3.红色节点的子节点必须是黑色节点
    4.从任意节点到其叶子节点的黑色节点数相等。
    特性：最长路径不大于最短路径的二倍
    :param val: 节点值
    :param color: 节点颜色
    '''

    def __init__(self, val, color="r"):

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

        print(str(self.val) + self.color, end=" ")
        if self.left:
            self.left.printf()
        if self.right:
            self.right.printf()

    def left_rotate(self):
        '''
        节点左旋
        需要在注意的地方就是，一个需要有一个子节点和一个父节点需要处理。
        而要处理的节点有三个因为ly没有保存所以先处理ly
        然后node rNode ，因为已经保存了引用，所以顺序可以随意处理
        :param node:
        :return:
        '''

        l = False  # 右子树
        fa = self.parent

        if fa and fa.left == self:
            l = True

        rNode = self.right

        if rNode.left:
            rNodeleft = rNode.left
            rNodeleft.parent = self
            self.right = rNodeleft
        else:
            self.right = None
        self.parent = rNode
        rNode.left = self
        if not fa:
            rNode.parent = None
            return
        if l:
            rNode.parent = fa
            fa.left = rNode
        else:
            rNode.parent = fa
            fa.right = rNode

    def right_rotate(self):
        '''
        右旋：左旋的反过来就是右旋
        :param node:
        :return:
        '''

        l = False  # 右子树
        fa = self.parent

        if fa and fa.left == self:
            l = True

        lNode = self.left

        if lNode.right:
            lNoderight = lNode.right
            lNoderight.parent = self
            self.left = lNoderight
        else:
            self.left = None
        self.parent = lNode
        lNode.right = self
        if not fa:
            lNode.parent = None
            return

        if l:
            lNode.parent = fa
            fa.left = lNode
        else:
            lNode.parent = fa
            fa.right = lNode

    def grandparent(self):
        return self.parent.parent

    def uncle(self):
        if self.parent == self.grandparent().left:
            return self.grandparent().right
        else:
            return self.grandparent().left


def insert(root: RBTree, val):
    if root.val == val:
        return
    if val > root.val:
        if not root.right:
            t = RBTree(val)
            root.right = t
            t.parent = root
            insert_case1(t)

        else:
            insert(root.right, val)
    elif val < root.val:
        if not root.left:
            t = RBTree(val)
            root.left = t
            t.parent = root
            insert_case1(t)

        else:
            insert(root.left, val)

    p = root
    while p.parent:
        p = p.parent
    return p


def insert_case1(node: RBTree):
    if not node.parent:
        node.setBlackNode()
    else:
        insert_case2(node)


def insert_case2(node: RBTree):
    if node.parent.isBlackNode():
        return
    else:
        insert_case3(node)


def insert_case3(node: RBTree):
    if node.uncle() != None and not node.uncle().isBlackNode():
        node.parent.setBlackNode()
        node.uncle().setBlackNode()
        node.grandparent().setRedNode()
        insert_case1(node.grandparent())
    else:
        insert_case4(node)


def insert_case4(node: RBTree):
    if node == node.parent.right and node.parent == node.grandparent().left:
        node.parent.left_rotate()
        node = node.left
    elif node == node.parent.left and node.parent == node.grandparent().right:
        node.parent.right_rotate()
        node = node.right
    insert_case5(node)


def insert_case5(node: RBTree):
    """
    插入情况5
    父节点是红色，叔叔节点为黑色或nil，而父节点又是祖父节点的左节点
    :param node:
    :return:
    """
    node.parent.setBlackNode()  # 交换父节点和祖父节点颜色
    node.grandparent().setRedNode()
    if node == node.parent.left and node.parent == node.grandparent().left:  # 祖父节点右旋
        node.grandparent().right_rotate()
    else:
        node.grandparent().left_rotate()


if __name__ == '__main__':
    root = RBTree(1)

    root.setBlackNode()

    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 5)
    # root = insert(root, 6)
    root.printf()
    print(root)
    # root.left = RBTree(3)
    # root.left.parent = root
    # root.left.left = RBTree(2)
    # root.left.left.setBlackNode()
    # root.left.left.parent = root.left
    # root.left.right = RBTree(5)
    # root.left.right.parent = root.left
    # root.left.right.setBlackNode()
    # root.left.right.left = RBTree(4)
    # root.left.right.left.parent = root.left.right
    # root.left.right.right = RBTree(6)
    # root.left.right.right.parent = root.left.right
    # root.printf()
    # print("\n")
    # root.left_rotate(root.left)
    # root.printf()
