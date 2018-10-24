# -*- coding: UTF-8 -*-
'''
加油站问题
'''
if __name__ == '__main__':
    list = [2, 1, 3, 4, 2, 1, 3, 1, 1, 3, 1, 1,1]  # 每个索引值代表在该点能加多少油

    s = []
    length = 0
    cl = 100
    def find(index, t, sum):
        global s
        global cl, length
        for i in range(index + 1, index + t + 1):
            if list[index] <= len(list) - i and index + t == i:
                # s[sum].append(i)
                print(i),
                length += 1
                find(i, list[i], sum + 1)
        print('\n')
        if length < cl:
            cl = length
            length = 0


    find(0, list[0], 0)

    min = 100
    for index in range(len(s)):
        if len(s[index]) < min:
            min = len(s[index])
    print('minxum: %d' % (min)),

    print(s)
