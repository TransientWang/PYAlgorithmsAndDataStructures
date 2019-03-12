# -*- coding: UTF-8 -*-
def quickSort(num, left, right):
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
    print(num)
    quickSort(num, left, i - 1)
    quickSort(num, i + 1, right)


if __name__ == '__main__':
    p = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    quickSort(p, 0, len(p) - 1)
    print(p)
