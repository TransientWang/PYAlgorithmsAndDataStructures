# -*- coding: UTF-8 -*-
from queue import Queue
class MyStack(object):

    def __init__(self):
        """
        225. 用队列实现栈
        Initialize your data structure here.
        """
        self.q_one = Queue()
        self.q_two = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q_one.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        count_one = self.q_one.qsize() - 1
        count_two = self.q_two.qsize() - 1
        if count_one != -1:
            for i in range(count_one):
                self.q_two.put(self.q_one.get())
            return self.q_one.get()
        elif count_two != -1:
            for i in range(count_two):
                self.q_one.put(self.q_two.get())
            return self.q_two.get()
        return None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        count_one = self.q_one.qsize() - 1
        count_two = self.q_two.qsize() - 1
        if count_one != -1:
            for i in range(count_one):
                self.q_two.put(self.q_one.get())
            t = self.q_one.get()
            self.q_two.put(t)
            return t
        elif count_two != -1:
            for i in range(count_two):
                self.q_one.put(self.q_two.get())
            t = self.q_two.get()
            self.q_one.put(t)
            return t
        return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q_one.qsize() + self.q_two.qsize() == 0


if __name__ == '__main__':
    st = MyStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.empty())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
