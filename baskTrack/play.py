# -*- coding: UTF-8 -*-
import math
class play:
    '''n皇后问题'''
    count = 0  # 结果数量
    n = 8;  # 皇后数量
    x = [0]  # x[i]表示第i个皇后在第几列
    def place(self, t):

        ok = True
        for i in range(0, t):
            if self.x[i] == self.x[t] or math.fabs(t - i) == math.fabs(self.x[t] - self.x[i]):
                ok = False
                break
        return ok

    #t是层数
    def backTrack(self, t):
        if t >= self.n:
            self.count+=1
            for i in range(0,len(self.x)):
                print((self.x[i]+1), end=' ')
            print('\n')
        else:
            #j是列数
            for j in range(0,self.n):
                self.x[t] = j
                if self.place(t):
                    self.backTrack(t+1)



if __name__ == '__main__':
    play =play()
    for i in range(1,play.n):
        play.x.append(-2)
    play.backTrack(0)
    print((play.count))
    print((play.__doc__))
