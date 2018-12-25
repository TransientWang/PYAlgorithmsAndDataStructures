# -*- coding: UTF-8 -*-


def majorityElement(self, nums):
    """
    给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    :type nums: List[int]
    :rtype: int
    """


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# def person(name, age, *, city, job):
#     print(name, age, city, job)
def aa(*argsl, **kwargs):
    print((argsl), end=' ')
    print(kwargs)


def fourSumCount(A, B, C, D):
    '''
     454.四数相加 II
    给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
    思路：分治思想：用hashMap存储 前两组的和以及重复次数
    在计算后两组倒数 在不在hashMap中，存在就加1
    :param A:
    :param B:
    :param C:
    :param D:
    :return:
    '''
    hMap = {}
    for i in range(len(A)):
        for j in range(len(A)):
            t = A[i] + B[j]
            hMap[t] = 0 if t not in hMap else hMap[t] + 1
    count = 0
    for i in range(len(A)):
        for j in range(len(A)):
            t = - (C[i] + D[j])
            count =count+ hMap[t] + 1 if t in hMap else count
    return count


if __name__ == '__main__':
    print(fourSumCount([1, 2],
                       [-2, -1],
                       [-1, 2],
                       [0, 2]))
