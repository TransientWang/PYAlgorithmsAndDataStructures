# -*- coding: UTF-8 -*-
def simplifyPath(path):
    """
    71. 简化路径
    思路：用栈处理问题 。
    将文件夹名 压入栈中
    :type path: str
    :rtype: str
    """
    path += "/"
    fd = ""  # 存储文件夹 和 ".\.."
    res = ""
    stack = []

    for i in path:
        if i == "/" and fd == "..":
            if stack:
                stack.pop()
            fd = ""
            continue
        elif i == "/" and fd == ".":
            fd = ""
            continue
        elif i == "/":
            if fd != "":
                stack.append(fd)
            fd = ""
            continue
        fd += i

    if not stack:
        return "/"
    while stack:
        res = res + "/" + stack.pop(0)

    return res


def removeDuplicates(nums):
    """
    80.删除排序数组中的重复项 II
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    while idx < len(nums):
        if idx < 2 or nums[idx] != nums[idx - 2]:
            idx += 1
        else:
            nums.pop(idx)
    return idx


def grayCode(n):
    """
    89. 格雷编码

    关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);
    如 n = 3:
    G(0) = 000,
    G(1) = 1 ^ 0 = 001 ^ 000 = 001
    G(2) = 2 ^ 1 = 010 ^ 001 = 011
    G(3) = 3 ^ 1 = 011 ^ 001 = 010
    G(4) = 4 ^ 2 = 100 ^ 010 = 110
    G(5) = 5 ^ 2 = 101 ^ 010 = 111
    G(6) = 6 ^ 3 = 110 ^ 011 = 101
    G(7) = 7 ^ 3 = 111 ^ 011 = 100
    每一位是 i 与 i 右移一位的异或结果
    :type n: int
    :rtype: List[int]
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


def findMin(nums):
    """
    153. 寻找旋转排序数组中的最小值
    二分法
    最小的数必然在无序的部分, 所以每次划分都进入无序的那一部分
    由于条件是 lo < hi 所以 hi 永远都不等于 mid, 但是 lo
    可能等于 mid, 例如 lo = 1, hi = 2, mid = 1. 所以每次
    和 hi 对应元素比较可以保证数组范围收敛到 1
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[high] < nums[mid]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


def findMin(nums):
    """
    154. 寻找旋转排序数组中的最小值 II
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[high] < nums[mid]:
            low = mid + 1
        elif nums[high] > nums[mid]:
            high = mid
        else:
            high -= 1
    return nums[low]


def maximumGap(nums):
    """
    164. 最大间距
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return 0

    Min = min(nums)
    Max = max(nums)
    if Min == Max:
        return 0

    bucket_Min = [None] * (len(nums) + 1)
    bucket_Max = [None] * (len(nums) + 1)
    bucket_hasnum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        idx = (nums[i] - Min) * len(nums) // (Max - Min)  #
        if not bucket_hasnum[idx]:
            bucket_Min[idx] = nums[i]
            bucket_Max[idx] = nums[i]
            bucket_hasnum[idx] = 1
        else:
            bucket_Min[idx] = min(bucket_Min[idx], nums[i])
            bucket_Max[idx] = max(bucket_Max[idx], nums[i])

    last = None
    Max = 0
    for i in range(len(nums) + 1):
        if bucket_hasnum[i]:
            if not last:
                last = bucket_Max[i]
            else:
                Max = max(Max, bucket_Min[i] - last)
                last = bucket_Max[i]
    return Max


if __name__ == '__main__':
    print(maximumGap([100,200,676767,13124,3453,333,3444]))
