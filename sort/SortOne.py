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
        if r.get(i, 0) == 0:
            r[i] = 1
        else:
            r[i] += 1
    array = [[key, r[key]] for key in r]
    array = sorted(array, key=lambda item: item[1], reverse=True)

    t = map(lambda item: item[0], array)
    return list(t)[:k]


def findPeakElement(nums):
    '''
    162	.寻找峰值
    峰值元素是指其值大于左右相邻值的元素。

    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

    你可以假设 nums[-1] = nums[n] = -∞。
    >>> findPeakElement([1, 2])
    :param self:
    :param nums:
    :return:
    '''
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid == len(nums) - 1:
            return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return right


def searchRange(nums, target):
    '''
    34.在排序数组中查找元素的第一个和最后一个位置
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

    你的算法时间复杂度必须是 O(log n) 级别。(二分法)

    如果数组中不存在目标值，返回 [-1, -1]。
    :param nums:
    :param target:
    :return:
    '''
    if len(nums) == 0:
        return [-1, -1]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[mid] != target:
        return [-1, -1]
    i = j = mid
    while i >= 0 and nums[i] == target:
        i -= 1
    while j < len(nums) and nums[j] == target:
        j += 1
    return [i + 1, j - 1]


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    '''
    给出一个区间的集合，请合并所有重叠的区间。
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    :param intervals:
    :return:
    '''
    intervals.sort(key=lambda item: item.start)
    i = 0
    while i < len(intervals) - 1:
        if intervals[i].end >= intervals[i + 1].start or intervals[i].start >= intervals[i + 1].start or intervals[
            i].end >= intervals[i + 1].end:
            s = intervals[i].start
            e = intervals[i].end
            if intervals[i].end >= intervals[i + 1].start:
                e = intervals[i + 1].end

            if intervals[i].start >= intervals[i + 1].start:
                s = intervals[i + 1].start
            if intervals[i].end >= intervals[i + 1].end:
                e = intervals[i].end
            intervals[i].start = s
            intervals[i].end = e
            intervals.remove(intervals[i + 1])
        else:
            i += 1
    return intervals


def search(nums, target):
    '''
    33.搜索旋转排序数组
    如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，
    我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了，代码如下
    :param nums:
    :param target:
    :return:
    '''
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[-1]:  # 左边有序
            if nums[left] <= target and nums[mid] > target:  # 通过两边边界值 确定新边界
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def searchMatrix(matrix, target):
    '''
    240.搜索二维矩阵 II
    左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素。比较左下角元素和目标：
    若左下角元素等于目标，则找到
    若左下角元素大于目标，则目标不可能存在于当前矩阵的最后一行，问题规模可以减小为在去掉最后一行的子矩阵中寻找目标
    若左下角元素小于目标，则目标不可能存在于当前矩阵的第一列，问题规模可以减小为在去掉第一列的子矩阵中寻找目标
    若最后矩阵减小为空，则说明不存在
    思路：类似二分法，但是需要找一个起始点，这个点可以从两边缩小范围，如果在左上角，那么只能坐标+1但不确定x还是y+1。
    左下角就可以小了+纵坐标 ，大了 - 横坐标
    :param target:
    :return:
    '''
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    x, y = len(matrix) - 1, 0

    while x >= 0 and y < len(matrix[0]):
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] < target:
            y += 1
        else:
            x -= 1
    return False





if __name__ == '__main__':
    print(searchRange([1, 4],
                      4))
