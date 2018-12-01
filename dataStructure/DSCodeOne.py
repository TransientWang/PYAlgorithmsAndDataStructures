# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


def maxPathSum(root):
    '''
    二叉树中的最大路径和
    给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
  注意：路径指的是不带分叉的一条路径

  由于这是一个很简单的例子，我们很容易就能找到最长路径为7-11-4-13，那么怎么用递归来找出正确的路径和呢？根据以往的经验，树的递归解法一般都是递归到叶节点，然后开始边处理边回溯到根节点。那么我们就假设此时已经递归到结点7了，那么其没有左右子节点，所以如果以结点7为根结点的子树最大路径和就是7。然后回溯到结点11，如果以结点11为根结点的子树，我们知道最大路径和为7+11+2=20。但是当回溯到结点4的时候，对于结点11来说，就不能同时取两条路径了，只能取左路径，或者是右路径，所以当根结点是4的时候，那么结点11只能取其左子结点7，因为7大于2。所以，对于每个结点来说，我们要知道经过其左子结点的path之和大还是经过右子节点的path之和大。那么我们的递归函数返回值就可以定义为以当前结点为根结点，到叶节点的最大路径之和，然后全局路径最大值放在参数中，用结果res来表示。

在递归函数中，如果当前结点不存在，那么直接返回0。否则就分别对其左右子节点调用递归函数，由于路径和有可能为负数，而我们当然不希望加上负的路径和，所以我们和0相比，取较大的那个，就是要么不加，加就要加正数。然后我们来更新全局最大值结果res，就是以左子结点为终点的最大path之和加上以右子结点为终点的最大path之和，还要加上当前结点值，这样就组成了一个条完整的路径。而我们返回值是取left和right中的较大值加上当前结点值，因为我们返回值的定义是以当前结点为终点的path之和，所以只能取left和right中较大的那个值，而不是两个都要。
---------------------
作者：雪过无痕_
来源：CSDN
原文：https://blog.csdn.net/weixin_40039738/article/details/79681446
版权声明：本文为博主原创文章，转载请附上博文链接！
    :param root:
    :return:
    '''
    sums = [-10000]

    def find(root, s):
        if not root:
            return 0
        l = max(find(root.left, s), 0)
        r = max(find(root.right, s), 0)
        s[0] = max(s[0], l + r + root.val)
        return max(l, r) + root.val

    find(root, sums)
    return sums[0]


def findCircleNum(M):
    '''
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
    DFS:维护一个已经遍历过得人的数组
    如果这个人没有遍历过，就标记已遍历，然后在图中搜索这一行中为1 ，且还没有遍历过得人，
    找到后继续对这个人标记，然后递归搜索
    :param self:
    :param M:
    :return:
    '''
    pass
    if M is None or len(M) == 0:
        return 0
    row = len(M)
    colum = len(M[0])
    visit = [False for i in range(row)]

    count = 0

    def find(x):
        for y in range(colum):
            if M[x][y] == 1 and visit[y] == 0:
                visit[y] = True
                find(y)

    for i in range(row):
        if visit[i] == False:
            find(i)
            count += 1

    return count


if __name__ == '__main__':
    print(findCircleNum([[1, 1, 0],
                         [1, 1, 1],
                         [0, 1, 1]]))