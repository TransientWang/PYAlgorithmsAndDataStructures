# -*- coding: UTF-8 -*-
from dataStructure import TreeNode
from dataStructure import ListNode


def sortedListToBST(head):
    """
    109. 有序链表转换二叉搜索树
    思路：遍历求长度，递归创建树
    :type head: ListNode
    :rtype: TreeNode
    """

    def create(tmp, l, r):
        if l > r:
            return None
        mid = (l + r) // 2  # 因为已经有序，平衡二叉树选取列表中点作为根节点就可以
        root = TreeNode.TreeNode(tmp[mid])
        root.left = create(tmp, l, mid - 1)
        root.right = create(tmp, mid + 1, r)
        return root

    p = head
    tmp = []
    while p:
        tmp.append(p.val)
        p = p.next

    return create(tmp, 0, len(tmp) - 1)


def isBalanced(root):
    """
    110. 平衡二叉树
    递归解决 -1 代表不是平衡二叉树
    :type root: TreeNode
    :rtype: bool
    """

    def find(root):
        if not root:
            return 0
        left = find(root.left)
        right = find(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + left if left > right else 1 + right

    if find(root) == -1:
        return False
    return True


def minDepth(root):
    """
    111. 二叉树的最小深度
    递归求深度当子节点为0的时候不应该参与计算
    :type root: TreeNode
    :rtype: int
    """

    def find(root):
        if not root:
            return 0
        left = find(root.left)
        right = find(root.right)
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1
        return min(left + 1, 1 + right)

    return find(root)


def hasPathSum(root, sum):
    """
    112. 路径总和（review）
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root == None:
        return False
    if root.left or root.right:
        res = hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)
        return res
    elif sum - root.val == 0:
        return True
    else:
        return False


def pathSum(root, sum):
    """
    113. 路径总和 II
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    res = []

    def find(root, t, tmp):
        if root.val + t == sum:
            if not root.left and not root.right:
                res.append(tmp + [root.val])

        if root.left:
            find(root.left, t + root.val, tmp + [root.val])
        if root.right:
            find(root.right, t + root.val, tmp + [root.val])

    if not root:
        return []
    find(root, 0, [])
    return res


def flatten(root):
    """
    114. 二叉树展开为链表
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    def dfs(root):
        if not root:
            return None
        left = dfs(root.left)
        right = dfs(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        if right:
            return right
        if left:
            return left
        return root

    dfs(root)


def rightSideView(root):
    """
    199. 二叉树的右视图
    队列
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    queue, res = [root], []

    while queue:
        lens = len(queue)
        for i in range(lens):
            tmp = queue.pop(0)
            if tmp.right:
                queue.append(tmp.right)
            if tmp.left:
                queue.append(tmp.left)
            if i == 0:
                res.append(tmp.val)
    return res


def lowestCommonAncestor(root, p, q):
    """
    235. 二叉搜索树的最近公共祖先(review)
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # if not root \
    #         or (p.val < root.val and q.val > root.val) \
    #         or (p.val > root.val and q.val < root.val) \
    #         or root.val == p.val \
    #         or root.val == q.val:
    #     return root
    #
    # if p.val > root.val:
    #     return lowestCommonAncestor(root.right, p, q)
    # else:
    #     return lowestCommonAncestor(root.left, p, q)
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    return root


if __name__ == '__main__':
    # head = ListNode.ListNode(1)
    # head.next = ListNode.ListNode(2)
    # head.next.next = ListNode.ListNode(3)
    # head.next.next.next = ListNode.ListNode(4)
    # head.next.next.next.next = ListNode.ListNode(5)
    # mid = head.next.next.next.next
    # mid.next = ListNode.ListNode(6)

    root = TreeNode.TreeNode(2)
    root.left = TreeNode.TreeNode(1)
    root.right = TreeNode.TreeNode(3)
    # root.left.left = TreeNode.TreeNode(0)
    # root.left.right = TreeNode.TreeNode(4)
    # root.right.left = TreeNode.TreeNode(7)
    # root.right.right = TreeNode.TreeNode(9)
    # root.left.left.left = TreeNode.TreeNode(-1)
    print(lowestCommonAncestor(root, TreeNode.TreeNode(3), TreeNode.TreeNode(1)))
