# -*- coding: UTF-8 -*-
import collections


def findItinerary(tickets: 'List[List[str]]') -> 'List[str]':
    """
    332. 重新安排行程(review)
    https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
    我们从'JFK'出发，一直按照lexical order往下走，比如从'JFK'可以去'SFO'和'ATL‘，那么我们优先去'ATL'
    边走边消除ticket，也就是说我们从'JFK'出发去了'ATL'，那么ticket ["JFK","ATL"]就没了
    然后走到某一个位置的时候我们发现往下走不下去了，我们就将当前卡住的位置放到最终结果route中去，然后我们倒退一步看看除了这条路还
    有没有别的路走， 继续这个过程，直到我们回到'JFK'，且没有路走了，我们就将route逆序返回，即是结果，因为route的第一个点其实是我们最后到的点
    :param tickets:
    :return:
    """
    lookup = collections.defaultdict(list)
    for start, end in tickets:
        lookup[start].append(end)
    for i in lookup.values():
        i.sort()
    # res = []
    # def dfs(lookup, from_, res):
    #     while lookup[from_]:
    #         v = lookup[from_].pop(0)
    #         dfs(lookup, v, res)
    #     res.append(from_)
    #
    # dfs(lookup, "JFK", res)
    # return res[::-1]

    route, stack = [], ['JFK']
    while stack:
        while lookup[stack[-1]]:
            stack.append(lookup[stack[-1]].pop(0))
        route.append(stack.pop())
    return route[::-1]


if __name__ == '__main__':
    print(findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
