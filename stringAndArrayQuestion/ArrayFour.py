# -*- coding: UTF-8 -*-
def combinationSum3(k, n):
    """
    216. 组合总和 III
    回溯
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    if n == 0:
        return 0
    res = []

    def find(s_list, begin, end):
        if len(s_list) > k:
            return
        if len(s_list) == k and sum(s_list) == n:
            res.append(s_list)
            return
        for i in range(begin, end):
            if len(s_list) == k:
                break
            find(s_list + [i], i + 1, end)

    find([], 1, min(n, 10))
    return res


if __name__ == '__main__':
    print(combinationSum3(3, 9))
