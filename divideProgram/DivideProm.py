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


if __name__ == '__main__':
    # g = (x * x for x in range(10))
    # print(g.next())
    # print(g.next())
    # print(g.next())
    # for i, value in enumerate(['A', 'B', 'C']):
    #
    #     print(i, value)
    # for x, y in [(1, 1), (2, 4), (3, 9)]:
    #     print(x, y)
    #
    # f = fib(6)
    # while True:
    #     try:
    #         x = f.next()
    #         print(x)
    #     except StopIteration as s:
    #         print(s.value)
    #         break
    r = {"mame": "王"}
    m = [1, 2, 4]
    aa(*m, **r)


    def fourSumCount(A, B, C, D):
        '''
         四数相加 II
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
        dpMap = {}
        for i in range(len(A)):
            for j in range(len(A)):
                t = (A[i] + B[j])
                dpMap[t] = 0 if t not in dpMap else dpMap[t] + 1
        count = 0
        for i in range(len(A)):
            for j in range(len(A)):
                t = -(C[i] + D[j])
                count = count + t + 1 if t in dpMap else count
        return count
