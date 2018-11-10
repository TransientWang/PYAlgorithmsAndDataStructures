# -*- coding: UTF-8 -*-
'''
最小栈
实现线性时间获取占中 最小值
思路：用一个数组存储最小值、
每次添加的时候遇到比最小值栈定小的就添加进栈
删除的时候，如果删除值与栈顶元素相等就弹出
不相等不做操作
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        item = self.stack.pop()
        if self.min and self.min[-1] == item:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        return None


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(2)

    minStack.push(3)
    minStack.push(1)
    print((minStack.getMin()))
    minStack.pop()
    minStack.pop()


    print((minStack.getMin()))
