# -*- coding: UTF-8 -*-
import math

'''
贪心算法
'''


class GreddySelector:

    def __init__(self,name):
        print("初始化")
        self.__myname = "王扶摇"

    __myname = ''
    wList = [2.0, 5.0, 8.0, 9.0, 5.0, 4.0, 5.0, 5.0, 5.0, 4.0]
    vList = [8.0, 15.0, 20.0, 18.0, 8.0, 6.0, 7.0, 6.0, 5.0, 3.0]
    m = 30

    def bagSolution(self,wList, vList, m):
        pList = []
        sum = 0
        for index in range(len(wList)):
            pList.append(float(vList[index] / wList[index]))

        pList.sort(reverse=True)

        for index in range(len(pList)):
            if m > wList[index]:
                m -= wList[index]
                sum += vList[index]
            else:
                sum += (m / wList[index] * vList[index])
                break

        return sum

    # print(bagSolution(wList, vList, m))


sel = GreddySelector()
print((sel.bagSolution(sel.wList,sel.vList,sel.m)))
