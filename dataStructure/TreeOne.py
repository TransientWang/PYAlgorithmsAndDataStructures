# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


def inorderTraversal(root):
    '''
    94.二叉树的中序遍历 TODO：迭代不熟悉
    给定一个二叉树，返回它的中序遍历。
    '''
    # res = []
    #
    # def find(root):
    #     if not root:
    #         return
    #     if root.left:
    #         find(root.left)
    #     res.append(root.val)
    #     if root.right:
    #         find(root.right)
    # find(root)
    # return res
    stack = []
    cur = root
    res = []
    while cur or len(stack):
        while cur:
            stack.append(cur)
            cur = cur.left
        if len(stack):
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


def zigzagLevelOrder(root):
    '''
    103.二叉树的锯齿形层次遍历
    注意直接反转结果，不要在在结束后在队列上反转，要每一步判断反转
    '''
    if not root:
        return []
    queue = [root]
    k = 0
    res = []
    while len(queue) != 0:
        t = []
        lens = len(queue)
        for i in range(lens):
            node = queue.pop(0)
            t.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if k % 2 == 1:
            t.reverse()
        k += 1

        res.append(t)
    return res


def buildTree(preorder, inorder):
    '''
    105.从前序与中序遍历序列构造二叉树
    思路：解决这个问题的是关键 是要明确二叉树的遍历是一个递归的过程
    根据前序遍历 可以得到 根节点
    那么在 中序遍历中  可以根据前序遍历得到的根节点 获得到 根节点的左右子树信息
    然后回到 前序遍历序列 中找到得到的左子树，那么在前序遍历中找到的左子树序列 也满足前序遍历序列
    他的第一个索引 也一样是左子树的头结点  这就是一个递归的过程
    :param preorder:
    :param inorder:
    :return:
    '''
    if not len(preorder) or not len(inorder):
        return None
    root = TreeNode.TreeNode(preorder[0])

    index_ = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:index_ + 1], inorder[:index_])
    root.right = buildTree(preorder[index_ + 1:], inorder[index_ + 1:])

    return root


def buildTreeOne(inorder, postorder):
    '''
    从中序与后序遍历序列构造二叉树
    :param inorder:
    :param postorder:
    :return:
    '''
    pass
    if len(inorder) == 0 or len(postorder) == 0:
        return None
    head = TreeNode.TreeNode(postorder[-1])
    i = inorder.index(postorder[-1])
    head.left = buildTreeOne(inorder[:i], postorder[:len(inorder[:i])])
    head.right = buildTreeOne(inorder[i + 1:], postorder[len(inorder[:i]):len(postorder) - 1])
    return head


class TreeLinkNode:
    '''
    每个节点的右向指针
    思路：此问题还是考察的二叉树层序遍历
    只要在每层遍历的过程中保存先前节点 并将 先前节点的下一个指向当前节点
    循环往复就可以
    '''

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if root is None:
        return None
    r = TreeLinkNode(1)
    mqueue = []

    mqueue.append(root)

    while len(mqueue) != 0:
        l = len(mqueue)
        tlNode = mqueue.pop(0)
        if tlNode.left is not None:
            mqueue.append(tlNode.left)
        if tlNode.right is not None:
            mqueue.append(tlNode.right)
        while l > 1:
            afNode = mqueue.pop(0)
            if afNode.left is not None:
                mqueue.append(afNode.left)
            if afNode.right is not None:
                mqueue.append(afNode.right)
            tlNode.next = afNode
            tlNode = afNode
            l -= 1
    return root


def count(root):
    '''
    二叉搜索树中第K小的元素
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    二叉搜索树：左子树上的节点都小于根节点的值，又子树的节点都大于根节点的值
    这是一个递归的过程
    思路：分治法，分为左右两边看，因为左边小所以先看左边
    先计算出左边节点数量
    分为三种情况
    一、当左边节点的数量+1 == k 说明 根节点就是我们要找的节点
    二、当左边节点数量>=k的时候，说明需要寻找的节点就在左子树上，
    这时只需要不断从上到下缩小左子树的查找范围，就能返回到第一中情况
    三、当左子树数量+1 < k 说明第k小的节点在右子树上 此时 需要查找右子树上第 k-左子树数量-1(根节点) 个节点即可
    '''
    if root is None:
        return 0
    else:
        return 1 + count(root.left) + count(root.right)


def kthSmallest(root, k):
    if root is None:
        return None

    lcount = count(root.left)

    if k == lcount + 1:
        return root.val
    elif k <= lcount:
        return kthSmallest(root.left, k)
    else:
        return kthSmallest(root.right, k - lcount - 1)


def numIslands(grid):
    '''
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
    并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
    思路：广度优先搜索 遍历地图，如果遇到1 则吧count+1 然后将其相邻为1的节点填充2
    :param grid:
    :return:
    '''
    if grid == []:
        return 0
    row = len(grid)
    colum = len(grid[0])

    def search(x, y):
        grid[x][y] = "2"
        if x + 1 < row and grid[x + 1][y] == "1":  # 右边
            search(x + 1, y)
        if x - 1 >= 0 and grid[x - 1][y] == "1":  # 左边
            search(x - 1, y)
        if y + 1 < colum and grid[x][y + 1] == "1":  # 上
            search(x, y + 1)
        if y - 1 >= 0 and grid[x][y - 1] == "1":  # 下
            search(x, y - 1)

    count = 0
    for i in range(row):
        for j in range(colum):
            if grid[i][j] == "1":
                count += 1
                search(i, j)
    print(grid)
    return count


if __name__ == '__main__':
    t = TreeNode.TreeNode(1)
    t.left = TreeNode.TreeNode(2)
    t.left.left = TreeNode.TreeNode(4)
    t.right = TreeNode.TreeNode(3)
    t.right.right = TreeNode.TreeNode(5)
    root = TreeLinkNode(1)
    # root.left = TreeLinkNode(2)
    # root.right = TreeLinkNode(3)
    head = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(head)
