# -*- coding: UTF-8 -*-

class NestedIterator(object):

    # def __init__(self, nestedList):
    #     """
    #     Initialize your data structure here.
    #     :type nestedList: List[NestedInteger]
    #     """
    #
    #     def flatten(nestedList):
    #         for x in nestedList:
    #             if x.isInteger():
    #                 yield x.getInteger()
    #             else:
    #                 for y in flatten(x.getList()):
    #                     yield y
    #
    #     self.gen = flatten(nestedList)
    #
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.val
    #
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     try:
    #
    #         self.val = next(self.gen)
    #         return True
    #     except StopIteration:
    #         return False

    def __init__(self, nestedList):
        """
        341.扁平化嵌套列表迭代器(review)
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        cur_nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return cur_nestedList[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            cur_nestedList, i = s[-1]
            if i == len(cur_nestedList):
                s.pop()
            else:
                x = cur_nestedList[i]
                if not hasattr(x,"__iter__"):  # x is a Integer
                    return True
                else:  # x is still a nestedList
                    s[-1][1] += 1
                    s.append([x, 0])
        return False





if __name__ == '__main__':
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext(): v.append(i.next())
    print(v)
