# -*- coding: UTF-8 -*-
import Queue


class Node:
    __cp = 0
    __rp = 0
    __rw = 0
    __id = 0
    _x = [0 for i in range(4)]

    def __init__(self, cp=0, rp=0, rw=0, id=0):
        self.__cp = cp
        self.__rp = rp
        self.__rw = rw
        self.__id = id

    def getCp(self):
        return self.__cp

    def setCp(self, cp):
        self.__cp = cp

    def getRp(self):
        return self.__rp

    def setRp(self, rp):
        self.__rp = rp

    def getRw(self):
        return self.__rw

    def setRw(self, rw):
        self.__rw = rw

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id


class goods:
    __weight = 0
    __value = 0

    def __init__(self, weight, value):
        self.__weight = weight
        self.__value = value

    def getWeight(self):
        return self.__weight

    def getValue(self):
        return self.__value

    def __str__(self):
        return "weight:" + str(self.__weight) + " value:" + str(self.__value)


if __name__ == '__main__':

    queue = Queue.Queue()
    list = [goods(2, 6), goods(5, 3), goods(4, 5), goods(2, 4)]
    t, tcp, trp, trw = 0, 0, 0, 0
    bestp, W, n, sumw, sumv = 0, 10, 0, 0, 0
    bestX = [0 for i in range(len(list))]
    queue.put(Node(0, sumv, W, 1))
    while not queue.empty():
        liveNode = queue.get()
        t = liveNode.getId()
        if t > len(list) - 1 or liveNode.getRw() == 0:
            if liveNode.getCp > bestp:
                for i in range(len(list)):
                    bestX[i] = liveNode._x[i]
                bestp = liveNode.getCp()
            continue

        if liveNode.getCp() + liveNode.getRp() < bestp:
            continue

        tcp = liveNode.getCp()
        trp = liveNode.getRp() - list[t].getValue()
        trw = liveNode.getRw()
        if trw >= list[t].getWeight():
            leftChild = Node(tcp + list[t].getValue(), trp, trw - list[t].getWeight(), t + 1)
            for i in range(t):
                leftChild._x[i] = liveNode._x[i]
            leftChild._x[t] = True
            if leftChild.getCp() > bestp:
                bestp = leftChild.getCp()
            queue.put(leftChild)

        if tcp + trp >= bestp:
            rightNode = Node(tcp, trp, trw, t + 1)
            for i in range(t):
                rightNode._x[i] = liveNode._x[i]
            rightNode._x[t] = False
            queue.put(rightNode)

    print('total:%d' % (bestp))
    for i in range(len(list)):
        if bestX[i]:
            print(i),
