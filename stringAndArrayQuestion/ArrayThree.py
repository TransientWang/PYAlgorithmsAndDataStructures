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
    桶排序
    思路：准备 n+1 和桶，每个桶中存放 3 个值，1、是否有元素 2、当前桶最大值看， 3、当前桶最小值
    最后一个桶 放最大值，省下的 (n-1)个元素放在面 n 个桶中，现在一定至少有一个桶为 空桶，而且中间有空桶的两侧的差值一定大
    于桶区间值，所以过滤掉了桶区间的计算。
    https://blog.csdn.net/zxzxzx0119/article/details/82889998
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
        idx = (nums[i] - Min) * len(nums) // (Max - Min)  # 每个桶的区间为 ( max-min) // 桶长度 ，每个元素落在的桶中，
        if not bucket_hasnum[  # idx 为 nums[i] // 桶区间    即：nums[i] //((max-min) // 桶长度） = nums[i] * 桶长度 // (max -min)
            idx]:
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


def twoSum(numbers, target):
    """
    167. 两数之和 II - 输入有序数组
    先二分缩小范围，再双指针
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    low, high = 0, len(numbers) - 1
    while low < high:
        mid = low + (high - low) // 2
        if numbers[mid] > target:
            high = mid
        else:
            low = mid + 1
    low, high = 0, low
    while low < high:
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            high -= 1


if __name__ == '__main__':
    print(twoSum([-3, 3, 4, 90],
                 0))
