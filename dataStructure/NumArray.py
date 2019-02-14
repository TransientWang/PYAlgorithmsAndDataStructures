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


if __name__ == '__main__':
    n = NumArray([1, 2, 3, 4, 5])
    print(n.sumRange(0, 4))
    n.update(1, 2)
    print(n.sumRange(0, 2))
