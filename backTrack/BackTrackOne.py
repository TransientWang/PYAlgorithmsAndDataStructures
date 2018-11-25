# -*- coding: UTF-8 -*-


def letterCombinations(digits):
    '''
    电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    :param digits:
    :return:
    '''
    res = []
    if digits == "":
        return res

    backTrack(0, digits, "", res)
    print(res)


def backTrack(h, digits, tmp, res):
    if h > len(digits) - 1:
        res.append(tmp)
        return
    number = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

    for i in range(len(number[int(digits[h])])):
        t = tmp + number[int(digits[h])][i]
        backTrack(h + 1, digits, t, res)


def generateParenthesis(n):
    '''
    生成括号
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
    例如，给出 n = 3，生成结果为
    如果用 暴力法，我们需要省城2的N次方个组合，然后筛选出来
    回溯法：可以只在判断括号是否有效之后再继续添加括号
    如果 左括号 数量小于n 就可以添加一个左括号
    如果 右括号数量 小于n就可以继续添加一个右括号
    :param n:
    :return:
    '''
    res = []

    def generateBackTrack(tmp="", left=0, right=0):
        '''

        :param tmp:
        :param left: 左括号的值
        :param right: 右括号的值
        :return:
        '''
        if len(tmp) == 2 * n:
            res.append(tmp)
            return
        if left < n:
            generateBackTrack(tmp + '(', left + 1, right)
        if right < left:
            generateBackTrack(tmp + ')', left, right + 1)

    generateBackTrack()
    print(res)

if __name__ == '__main__':
    generateParenthesis(3)
