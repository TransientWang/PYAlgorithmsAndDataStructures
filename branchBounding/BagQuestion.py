# -*- coding: UTF-8 -*-
import Queue


class Node:
    __cp = 0
    __rp = 0
    __rw = 0
    __id = 0
    __x = [True for i in range(4)]

    def __init__(self, cp=0, rp=0, rw=0, id=0):
        self.__cp = cp
        self.__rp = rp
        self.__rw = rw
        self.__id = id
        self.__x = [True for i in range(4)]

    def setX(self, index, bol):
        self.__x[index] = bol

    def getX(self, index):
        return self.__x[index]

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
    t, tcp, trp, trw = 0, 0, 0, 0  # t:当前处理的序号tcp:当前状物购物车物品价值 trp:当前剩余物品价值 trw:当前剩余容量
    bestp, W, n, sumw, sumv = 0, 10, 0, 13, 18  # bestp当前最优值 W购物车承重  sumw 当前重量 sumv当前价值
    bestX = [False for i in range(len(list))]  # 记录结果 哪些装了
    queue.put(Node(0, sumv, W, 0))
    while not queue.empty():
        liveNode = queue.get()
        t = liveNode.getId()
        # 搜到最后一个物品进行结算
        if t > len(list) - 1 or liveNode.getRw() == 0:
            if liveNode.getCp() >= bestp:
                for i in range(len(list)):
                    bestX[i] = liveNode.getX(i)
                bestp = liveNode.getCp()
            continue
        # 剪枝条件 当前价值 加上剩余价值  没有最优价值大的话就不用计算了
        if liveNode.getCp() + liveNode.getRp() < bestp:
            continue

        tcp = liveNode.getCp()  # 当前购物车中的价值
        trp = liveNode.getRp() - list[t].getValue()  # 剩余价值，不管转入与否，当前剩余价值都会减少
        trw = liveNode.getRw()  # 剩余容量

        if trw >= list[t].getWeight():  # 满足条件的才会装入购物车
            leftChild = Node(tcp + list[t].getValue(), trp, trw - list[t].getWeight(), t + 1)  # 下一节点 传递参数
            for i in range(0, t):
                leftChild.setX(i, liveNode.getX(i))  # 复制之前的解向量
            leftChild.setX(t, True)
            if leftChild.getCp() >= bestp:  # 比最优值大就更新
                bestp = leftChild.getCp()
            queue.put(leftChild)  # 做孩子入队

        # 扩展右孩子
        if tcp + trp >= bestp:  # 满足条件不放入购物车
            rightChild = Node(tcp, trp, trw, t + 1)  # 向下传递参数
            for i in range(0, t):
                rightChild.setX(i, liveNode.getX(i))  # 复制解向量

            rightChild.setX(t, False)
            queue.put(rightChild)  # 右孩子入队
    # TODO  这个算法还没有彻底理解，应当在看看
    print('total:%d' % (bestp))
    for i in range(len(list)):
        # if bestX[i]:
        print(bestX[i]),
