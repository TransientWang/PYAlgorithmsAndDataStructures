# -*- coding: UTF-8 -*-

if __name__ == '__main__':


    def counts():
        fs = []
        def f(j):                   #当调用f时，已经把变量i的副本传递给新创建的f函数，所以迭代一次 j 值就会增加一次
            def g():
                return j * j
            return g
        for i in range(1, 4):
            fs.append(f(i))
        return fs
    f1,f2,f3 =counts()        #fs里的f函数在此计算好，并赋值给f1=f(1).f2=f(2).f3=f(3)
    print(counts()[0]())
    print(f2())
    print(f3())

    def counts1():
        fs = []
        for i in range(1, 4):     #for循环在第一次调用counts1时候就已经执行完毕，返回值是三个新创建的g函数
                                  #但是g函数所访问到的变量i确是，最后一次循环得到的i,所以返回值永远是9
            def g():
                return i * i
            fs.append(g)
        return fs


    print(counts1()) #返回值是g函数
    print(counts1()[0]())      #与调用下面1语句相同效果
    # f11,f21,f31 =counts1()
    # print(f11())            1
    # print(f21())
    # print(f31())