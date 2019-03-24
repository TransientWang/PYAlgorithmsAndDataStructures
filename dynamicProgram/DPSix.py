# -*- coding: UTF-8 -*-
from typing import List


def numberOfArithmeticSlices(self, A: List[int]) -> int:
    #413. 等差数列划分
    n = len(A)
    res = 0
    r = 0
    for i in range(2, n):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            r += 1
            res += r
        else:
            r = 0
    return res