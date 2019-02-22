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
            count = count + hMap[t] + 1 if t in hMap else count
    return count


def countRangeSum(nums, lower, upper):
    """
    327. 区间和的个数
    :param nums:
    :param lower:
    :param upper:
    :return:
    """
    # 动态规划 TLE
    # nums.sort()
    # dp = [[0] * len(nums) for i in range(len(nums))]
    # sum = 0
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         dp[i][j] = nums[j] + dp[i][j - 1]
    #         if dp[i][j] >= lower and dp[i][j] <= upper:
    #             sum += 1
    # return sum

    # 分治法，通过分治法将范围不断缩小，由递归函数处理每一块较小的范围
    sums = [0]
    for i in nums:
        sums.append(sums[-1] + i)

    def sort(lo, hi):
        if hi - lo <= 1:  # 如果数组只有一个数，那么下面的算法将不能比较出来，还会将数组长度退化成1，在下面的 sort 会栈溢出
            return 0

        mid = (lo + hi) // 2
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid  # 放在for 循环的外面，已经计算过的就不再重复，减少计算量
        for left in sums[lo:mid]:  # 对于 lo:mid 和 mid:hi 的所有情况已经在递归中全部计算过了，现在只有右边减去左边的可能没有出现过
            while i < hi and sums[i] - left < lower: i += 1
            while j < hi and sums[j] - left <= upper: j += 1
            count += j - i
        sums[lo:hi] = sorted(sums[lo:hi])  # 如果不排序，就会出现前面较大的数sums[h] (h >=mid)
        # 在索引低位的数 left计算失败后，left后移，而后面较小的数 sums[h+1] 计算不到 left 的情况的情况
        return count

    return sort(0, len(sums))


def reversePairs(nums):
    """
    493. 翻转对
    归并
    :type nums: List[int]
    :rtype: int
    """

    def find(lo, hi):
        if lo == hi:
            return 0

        count = 0
        mid = (lo + hi) // 2
        count += find(lo, mid) + find(mid + 1, hi)
        left = lo
        right = mid + 1
        while left <= mid and right <= hi:
            if nums[left] > 2 * nums[right]:
                # 如果我们找到了有效对，则left和mid之间的元素也将是有效对。计算这些元素
                count += mid - left + 1
                # 增加右指针以检查左侧元素是否可以与其中任何一个匹配
                right += 1
            else:
                left += 1
        # 核心
        nums[lo: hi + 1] = sorted(nums[lo: hi + 1])  # 排序是因为 mid 左右两边在比较的时候可以节省时间，否则需要 o(n^2)
        return count

    if not nums:
        return 0

    return find(0, len(nums) - 1)


if __name__ == '__main__':
    print(reversePairs([2, 2, -2, -2, -2, 2]))
