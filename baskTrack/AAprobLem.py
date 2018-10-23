# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    list = [30, 40, 60, 70,10,196]
    mList = []
    r = [[0 for i in range(len(list))] for i in range(len(list))]  # 辅助数组 r[i][j] 代表i应该给j的钱数
    mid = 0
    for i in range(0, len(list)):
        mid += list[i]
    mid /= len(list);
    print(mid)
    for i in range(0, len(list)):
        mList.append(mid - list[i])
    print(mList)
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if i == j:
                continue
            else:
                if mList[i] < 0 and mList[j] > 0:
                    mList[i] += mList[j]
                    r[j][i] = mList[j]
                    mList[j] -= mList[j]

    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if r[i][j] <> 0:
                print(i, " gave ",r[i][j]," to ", j)
    print(mList)