# -*- coding: UTF-8 -*-
def quickSort(num, left, right):
    """
    快速排序
    :param num:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return
    i, j, tmp = left, right, num[left]
    while i < j:
        while i < j and num[j] >= tmp:  # 一定要带上等于号
            j -= 1
        while i < j and num[i] <= tmp:
            i += 1
        if i < j:
            t = num[j]
            num[j] = num[i]
            num[i] = t
    num[left] = num[i]
    num[i] = tmp
    quickSort(num, left, i - 1)
    quickSort(num, i + 1, right)


def mergeSort(num, left, right):
    """
    归并排序
    :param num:
    :param left:
    :param right:
    :return:
    """

    def merge(num, left, mid, right):
        tmp = [0] * (right - left + 1)
        i = left

        j = mid + 1
        idx = 0
        while i <= mid and j <= right:
            if num[i] > num[j]:
                tmp[idx] = num[j]
                j += 1
            else:
                tmp[idx] = num[i]
                i += 1
            idx += 1
        while i <= mid:
            tmp[idx] = num[i]
            idx += 1
            i += 1
        while j <= right:
            tmp[idx] = num[j]
            j += 1
            idx += 1
        num[left:right + 1] = tmp

    if left >= right:
        return
    mid = (left + right) // 2

    mergeSort(num, left, mid)
    mergeSort(num, mid + 1, right)
    merge(num, left, mid, right)


def bubbleSort(num):
    """
    冒泡排序
    :param num:
    :return:
    """
    for i in range(len(num) - 1, -1, -1):
        for j in range(i):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]


def insertSort(num):
    """
    插入排序
    :param num:
    :return:
    """
    for i in range(len(num)):
        t = num[i]
        j = i - 1
        while j >= 0 and t < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = t


def shellSort(arr):
    """
    希尔排序
    :param arr:
    :return:
    """
    h = len(arr) // 3

    while h >= 1:
        for i in range(h, len(arr)):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = h // 3


def selectSort(num):
    """
    选择排序
    :param num:
    :return:
    """
    for i in range(len(num)):
        t = i
        for j in range(i, len(num)):
            if num[t] > num[j]:
                t = j
        num[i], num[t] = num[t], num[i]


def heapSort(num):
    """
    堆排序
    :param num:
    :return:
    """

    def buildHeap(num):
        for i in range(len(num) // 2 - 1, -1, -1):
            heapAdjust(i, num, len(num))

    def heapAdjust(idx, num, lens):
        left = idx * 2 + 1
        right = idx * 2 + 2
        if left < lens and num[idx] > num[left]:
            num[idx], num[left] = num[left], num[idx]
            heapAdjust(left, num, lens)

        if right < lens and num[idx] > num[right]:
            num[idx], num[right] = num[right], num[idx]
            heapAdjust(right, num, lens)

    buildHeap(num)
    for i in range(len(num) - 1, -1, -1):
        num[0], num[i] = num[i], num[0]
        heapAdjust(0, num, i)


def countSort(num):
    """
    计数排序
    :param num:
    :return:
    """
    min_ = max_ = 0
    for i in num:
        min_ = min(min_, i)
        max_ = max(max_, i)
    tmp = [0] * (max_ - min_)
    for i in num:
        tmp[i - min_ - 1] += 1
    res = []
    for i in range(len(tmp)):
        while tmp[i] >= 1:
            res.append(min_ + i+1)
            tmp[i] -= 1
    return res


if __name__ == '__main__':
    p = [9, 8, 7, 6, 5, 4, 3, 1, 2]

    print(countSort(p))
