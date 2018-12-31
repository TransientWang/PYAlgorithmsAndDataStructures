# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


def maxPathSum(root):
    '''
    findCircleNum
    DFS
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

    def find(root, sums):
        if not root:
            return 0
        left = max(find(root.left, sums), 0)
        right = max(find(root.right, sums), 0)
        sums[0] = max(sums[0], left + right + root.val)
        return max(left, right) + root.val

    sums = [-1000]
    find(root, sums)
    return sums[0]


def findCircleNum(M):
    '''
    547.Friend Circles
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
    DFS:维护一个已经遍历过得人的数组
    如果这个人没有遍历过，就标记已遍历，然后在图中搜索这一行中为1 ，且还没有遍历过得人，
    找到后继续对这个人标记，然后递归搜索
    :param self:
    :param M:
    :return:
    '''
    if M is None or len(M) == 0:
        return 0
    row = len(M)
    visited = [False for i in range(row)]

    def find(x):
        for y in range(row):
            if M[x][y] == 1 and visited[y] == False:
                visited[y] = True
                find(y)

    count = 0
    for i in range(row):
        if visited[i] == False:
            find(i)
            count += 1
    return count


def longestIncreasingPath(matrix):
    '''
     329.矩阵中的最长递增路径
     给定一个整数矩阵，找出最长递增路径的长度。

    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
    思路：这道题考察了DFS和动态规划，因为需要计算每一个点的最大长度，如果只用DFS计算就会超时
    解决办法就是动态规划
    用一个数组来保存[x,y]点的最长长度，当计算到某个点的时候 如果辅助数组上该点不为0那么就代表该点已经计算过了，
    直接返回该点的数值，如果该点没有计算过，则dfs计算 当前点符合条件的时候用下一个节点计算的返回值+1就是当前节点的
    最大值。然后比较求出周围四个点中最大的点，返回其值
    :param matrix:
    :return:
    '''
    if len(matrix) == 0 or matrix is None:
        return 0
    direct = ((1, 0), (-1, 0), (0, 1), (0, -1))
    row = len(matrix)
    colum = len(matrix[0])
    hMap = [[0 for i in range(colum)] for i in range(row)]

    def find(x, y):
        if hMap[x][y] != 0:
            return hMap[x][y]
        res = 1
        for i in direct:
            k = x + i[0]
            v = y + i[1]
            if k >= 0 and k < row and v >= 0 and v < colum and matrix[k][v] > matrix[x][y]:
                lens = 1 + find(k, v)
                res = max(lens, res)
        hMap[x][y] = res
        return res

    max_res = 1
    for i in range(row):
        for j in range(colum):
            max_res = max(max_res, find(i, j))
    for i in range(row):
        print(hMap[i])
    return max_res


def countSmaller(nums):
    '''
    315.计算右侧小于当前元素的个数
    给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量
    思路：插入排序，存储元素在排序数组中的位置，用二分提高时间复杂度
    :param nums:
    :return:
    '''
    tmp = []
    t = [0 for i in range(len(nums))]

    def serarch(key, index):
        left, right = 0, len(tmp)
        while left < right:
            mid = left + (right - left) // 2
            if key < tmp[mid]:
                right = mid
            else:
                left = mid + 1
        tmp.insert(left, key)
        t[index] = left
    nums.reverse() # 从右侧开始找
    for i in range(len(nums)):
        serarch(nums[i], i)
    t.reverse()
    return t


import collections


def canFinish(numCourses, prerequisites):
    """
    207.课程表
    现在你总共有 n 门课需要选，记为 0 到 n-1。

    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

    给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
    思路：通过DFS，判断是否有拓补排序
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    visited = [0 for i in range(numCourses)]
    hmap = {i[0]: i[1:] for i in prerequisites}  # 邻接表

    def dfs(cur):
        if visited[cur] == 1:  # 当前节点正在被搜索，但是还没有搜索完毕
            return True
        if visited[cur] == 2:  # 当前节点已经被搜索完毕
            return False
        visited[cur] = 1
        if hmap.get(cur) != None:
            for i in hmap[cur]:
                if dfs(i):  # 如果该节点的后继节点是1，说明有环。直接返回True,则该节点不会被标记成2,
                    return True

        visited[cur] = 2
        return False

    for i in range(numCourses):
        if dfs(i):
            return False

    return True


def canFinishOne(numCourses, prerequisites):
    in_count = [0 for i in range(numCourses)]  # 出度
    record = [[] for i in range(numCourses)]
    for i in prerequisites:
        in_count[i[0]] = in_count[i[0]] + 1
        record[i[1]].append(i[0])

    que = []
    for i in range(len(in_count)):
        if (in_count[i] == 0):
            que.append(i)

    while (que):
        node = que.pop(0)
        for i in record[node]:
            in_count[i] = in_count[i] - 1
            if (in_count[i] == 0):
                que.append(i)

    if (sum(in_count)):
        return False
    else:
        return True


def findOrder(numCourses, prerequisites):
    """
     210.课程表 II
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    visit = [0 for i in range(numCourses)]
    hMap = {i[0]: [] for i in prerequisites}
    for i in prerequisites:
        hMap[i[0]].append(i[1])
    res = []

    def find(x):
        if visit[x] == 1:
            return True
        if visit[x] == 2:
            return False
        visit[x] = 1
        if x in hMap:
            for i in hMap[x]:
                if find(i):
                    return True
        res.append(x)
        visit[x] = 2
        return False

    for i in range(numCourses):
        if find(i):
            return []
    return res


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    root.right = TreeNode.TreeNode(3)
    print(countSmaller([5, 2, 6, 1]))
