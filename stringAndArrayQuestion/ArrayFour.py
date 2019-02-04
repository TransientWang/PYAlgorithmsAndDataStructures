# -*- coding: UTF-8 -*-
def combinationSum3(k, n):
    """
    216. 组合总和 III
    回溯
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []

    def find(s_list, begin, end):
        if len(s_list) == k:
            if sum(s_list) == n:
                res.append(s_list)
            return
        for i in range(begin, end):
            find(s_list + [i], i + 1, end)

    find([], 1, min(n, 10))
    return res


if __name__ == '__main__':
    print(combinationSum3(3, 9))
