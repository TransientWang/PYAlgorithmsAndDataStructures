# -*- coding: UTF-8 -*-
def swap(arr, a, b):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t


def heapAdjust(arr, index):
    left, right = index * 2 + 1, index * 2 + 2
    if left < len(arr) and arr[left][0] > arr[index][0]:
        swap(arr, left, index)
        heapAdjust(arr, left)
    if right < len(arr) and arr[right][0] > arr[index][0]:
        swap(arr, right, index)
        heapAdjust(arr, right)


def buildHeap(arr):
    lastIndex = int(len(arr) / 2)
    for i in range(lastIndex):
        index = lastIndex - 1 - i
        heapAdjust(arr, index)


def heapSort(arr, k):
    buildHeap(arr)
    res = []
    for i in range(k):
        t = len(arr) - i - 1
        swap(arr, 0, len(arr) - 1)
        res.append(arr.pop()[1])
        heapAdjust(arr, 0)
    return res

def sortCount(nums, min, max):
    '''
    计数排序：
    思想：首先需要知道这个数组中的最大值和最小值分别是多少
    然后维护一个 max-min+1的数组 用于保存 索引位置数-min 在待排序数组里的每一个数字数组出现的此时
    辅助数组索引就是待排序数组每个数字按大小顺序排列出现的次数了
    然后通过辅助数组来重新构建
    数组的索引加上最小值就是原数组的数字
    :param nums: 待排序数组
    :param min: 数组中的最小值
    :param max: 数组中的最大值
    :return:
    '''
    tmp = [0 for i in range(max - min + 1)]
    for i in nums:
        tmp[i - min] += 1
    q = 0
    for i in range(len(tmp)):
        while tmp[i] > 0:
            nums[q] = i
            q += 1
            tmp[i] -= 1

    print(nums)


def topKFrequent(nums, k):
    '''
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
    思路：用堆排序和hash(字典)来解决
    先用一个字典记录每个元素出现的次数
    再将 字典的val key转换成数组
    用堆排序 输出 出现次数前k的key值
    :param nums:
    :param k:
    :return:
    '''
    r = {}
    for i in nums:
        if r.get(i) is None:
            r[i] = 1
        else:
            r[i] += 1
    d = []
    for key, val in r.items():
        d.append((val, key))
    return heapSort(d, k)


if __name__ == '__main__':
    print(topKFrequent([1, 1, 1, 2, 2, 3],
                       2))
    # arr = [1, 1, 1, 2, 2, 3]
    # heapSort(arr)
