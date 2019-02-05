# -*- coding: UTF-8 -*-
class MyQueue:

    def __init__(self):
        """
        232. 用栈实现队列
        Initialize your data structure here.
        """
        self.stack_one = []
        self.stack_two = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_one.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        count_one = len(self.stack_one)
        if count_one != 0 and len(self.stack_two) == 0:
            for i in range(count_one - 1):
                self.stack_two.append(self.stack_one.pop())
            return self.stack_one.pop()
        if len(self.stack_two) != 0:
            return self.stack_two.pop()
        return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        count_one = len(self.stack_one)
        if count_one != 0 and len(self.stack_two) == 0:
            for i in range(count_one):
                self.stack_two.append(self.stack_one.pop())

        if len(self.stack_two) != 0:
            t = self.stack_two.pop()
            self.stack_two.append(t)
            return t
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack_one) + len(self.stack_two) == 0


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)

    print(q.peek())
    print(q.pop())
    print(q.empty())
