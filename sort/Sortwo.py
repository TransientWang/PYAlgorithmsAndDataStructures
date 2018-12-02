# -*- coding: UTF-8 -*-

import copy


def wiggleSort(nums):
    '''
    摆动排序
    :param nums:
    :return:
    '''
    t = copy.deepcopy(nums)
    t.sort()
    lens = len(nums)
    i = 1
    tmp = [0 for i in range(lens)]
    while i < lens:
        tmp[i] = t.pop()
        i += 2
    i = 0
    while i < lens:
        tmp[i] = t.pop()
        i += 2
    return tmp


if __name__ == '__main__':
    wiggleSort([1, 5, 1, 1, 6, 4])
