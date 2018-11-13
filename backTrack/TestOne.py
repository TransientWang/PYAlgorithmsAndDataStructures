# -*- coding: UTF-8 -*-
import unittest
import math


class MyTestCase(unittest.TestCase):
    count = 0  # 结果数量
    n = 8;  # 皇后数量
    x = [-1, -1, -1, -1, -1, -1, -1, -1]  # x[i]表示第i个皇后在第几列

    def test_something(self):
        self.assertEqual(True, True)

    def test_eightQueen(self):
        self.backTrack(0)

    def place(self, t):
        print((self.x[t]))
        ok = True
        for i in range(0, self.n):
            if self.x[i] == self.x[t] and t - i == math.fabs(self.x[t] - self.x[i]):
                ok = False
                break
        return ok

    def backTrack(self, t):
        if t >= self.n:
            self.count += 1
            for i in range(0, len(self.x)):
                print((self.x[i]), end=' ')
            print()
        else:
            for j in range(0, self.n):
                self.x[t] = j
                if self.place(t):
                    self.backTrack(t + 1)


'''
电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''


def letterCombinations(digits):
    res = []
    backTrack(0,digits,"",res)
    print(res)
def backTrack(h, digits, tmp, res):
    if h > len(digits)+1:
        res.append(tmp)
        return
    number = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    s="dawd"
    for i in range(3):
        number[digits[h]+2][i]
        t = tmp + number[digits[h]+2][i]
        backTrack(h+1,digits,tmp,res)


if __name__ == '__main__':
    letterCombinations("23")
