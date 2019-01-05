# -*- coding: UTF-8 -*-

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        def flatten(l):
            for el in l:
                if hasattr(el, "__iter__"):
                    for sub in flatten(el):
                        yield sub
                else:
                    yield el

        self.f_list = [i for i in flatten(nestedList)]
        self.count = -1
        self.lens = len(self.f_list)

    def next(self):
        """
        :rtype: int
        """
        if self.count < self.lens:
            self.count+= 1
            return self.f_list[self.count]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count < self.lens-1

    # def __init__(self, nestedList):
    #     """
    #     341.扁平化嵌套列表迭代器
    #     Initialize your data structure here.
    #     :type nestedList: List[NestedInteger]
    #     """
    #     self.stack = [[nestedList, 0]]
    #
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     cur_nestedList, i = self.stack[-1]
    #     self.stack[-1][1] += 1
    #     return cur_nestedList[i]
    #
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     s = self.stack
    #     while s:
    #         cur_nestedList, i = s[-1]
    #         if i == len(cur_nestedList):
    #             s.pop()
    #         else:
    #             x = cur_nestedList[i]
    #             if not hasattr(x,"__iter__"):  # x is a Integer
    #                 return True
    #             else:  # x is still a nestedList
    #                 s[-1][1] += 1
    #                 s.append([x, 0])
    #     return False





if __name__ == '__main__':
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext(): v.append(i.next())
    print(v)
