# -*- coding: UTF-8 -*-
class NumArray:
    def __init__(self, nums):
        """
        307. 区域和检索 - 数组可修改
        构造一棵线段树，可以按完全二叉树的结构构建，最多需要 2*n -1 个节点存储，
        所以可以使用相应长度的数组来存储它，
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = nums[:]  # 叶子节点在右侧 ，这样从根节点层到最后一层，一次从左王右排列
        for i in range(self.n - 1, 0, -1):  # 自底向上构建线段树
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i // 2] = self.tree[i // 2 * 2] + self.tree[i // 2 * 2 + 1]
            i //= 2  # 跳到上一层计算

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # 1、在叶子节点中找到左右边界的索引
        i, j = self.n + i, self.n + j
        sum_ = 0
        while i <= j:
            if i % 2 == 1:
                sum_ += self.tree[i]  # 左边没有参与计算
                i += 1
            if j % 2 == 0:
                sum_ += self.tree[j]  # 右边没有参与计算
                j -= 1
            i //= 2
            j //= 2
        return sum_


import collections


def findMinHeightTrees(n=5, edges=[[0, 1], [0, 2], [0, 3], [3, 4]]):
    """
    310. 最小高度树
    首先我们要找到一棵树，使得它的高度最短
    并且这是一个联通的图，因此我们试图找到一个点，从它往外延伸出去的距离最短，那么这样一个点势必就是整个图的中心点。
    换句话说，如果这个图当中有一条最长路径的话，那么这个最长路径的中点就是我们要找的那个点，
    当最长路径长度为奇数时（因为这个时候最长路径上的点的个数就是奇数），这样的中点有两个

    是我们已经把这个图看成一棵树了，那么树肯定会有叶子节点，我们一层一层删除掉叶子节点，
    然后去除他们与上一层的关系， 然后上一层又变成叶子节点了，重复这个步骤，直到节点只剩下一个或者两个，
    因为按照思路一里面的论证，最后的中点只会有一个或者两个
    一定要将无向图表达出来
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n <= 1:
        return [0]

    graph = collections.defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    leaves = [i for i in range(n) if len(graph[i]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            node = graph[leaf].pop()
            graph[node].remove(leaf)
            if len(graph[node]) == 1:
                new_leaves.append(node)
        leaves = new_leaves

    return leaves


if __name__ == '__main__':
    print(findMinHeightTrees())
