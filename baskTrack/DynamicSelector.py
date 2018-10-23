# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    r = [[0, 2, 6, 9, 15, 20],
         [0, 0, 3, 5, 11, 18],
         [0, 0, 0, 3, 6, 12],
         [0, 0, 0, 0, 5, 8],
         [0, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 0, 0]]  # 二维数组r[i][j]代表从i到j需要花的租金
    s = [[0, 0, 0, 0, 0, 0] for i in range(0, 6)]
    min = 1000  # 最小租金
    wmin = 0  # 当前最少租金
    m = [-1, -1, -1, -1, -1, -1]
    aft = [0]  # 存放每一步后驱
    n = len(r[0])
    temp = 0
    for d in range(3, n + 1):  # 将问题的规模缩小，初始只有三个点需要计算，然后递增一
        for i in range(0, n - d + 1):  # i计算的左边界
            j = i + d - 1  # j计算的右边界
            for k in range(i + 1, j + 1):  # k记录i,j之间的计算值
                temp = r[i][k] + r[k][j]
                if temp < r[i][j]:
                    r[i][j] = temp
                    s[i][j] = k
                    # r[i][j] = r[i][k] + r[k][j]

                    # m[i][j] = temp[0]

    for i in range(0, 6):
        for j in range(0, 6):
            if s[i][j] <> 0:
                print(s[i][j]),
            else:
                print(s[i][j]),
        print("\n")

    print('1'),


    def read(i, j):
        if s[i][j] == 0:
            print('--'),
            print(j + 1),
            return
        read(i, s[i][j])
        read(s[i][j], j)


    read(0, 5)
