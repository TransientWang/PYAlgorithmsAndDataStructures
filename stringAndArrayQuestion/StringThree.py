# -*- coding: UTF-8 -*-

def minWindow(s, t):
    '''
    最小窗口子字符串
    给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

    TODO 双指针是求解字符串问题的通用解法
    :param s:
    :param t:
    :return:
    '''
    if len(s) < len(t) or len(s) == 0 or s is None or t is None or len(t) == 0:
        return ""
    start, end = 0, 0
    cstart = 0
    hmap = [0 for i in range(188)]  # 定义一个可以容纳所有ASCII字母的数组
    for i in t:
        hmap[ord(i)] += 1  # 在t串中的字符出现一次+1
    count = 0
    res = 2 ** 31
    while end < len(s):
        if hmap[ord(s[end])] > 0:  # 匹配count+1
            count += 1
        hmap[ord(s[end])] -= 1  # 尾指针遍历过得出现次数-1
        end += 1  # 尾指针后移
        while count == len(t):  # 找到完全匹配的字符串的时候
            if end - start < res:  # 记录最短长度
                res = end - start
                cstart = start
            if hmap[ord(s[start])] == 0:  # 如果首字符==0说明，手指针字符在t中。count-1
                count -= 1
            hmap[ord(s[start])] += 1  # 手指针遍历过得字符次数+1，还原（针对t中的字符）
            start += 1  # 手指针后移
    res = 0 if res == 2 ** 31 else res
    return s[cstart:cstart + res]


def calculate(s):
    '''
    基本计算器 II
    实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
思路：用栈来存储数字，由于涉及到优先级，所以遇到减号
 将后面的数字变成负值入栈，乘除法先计算，加减法遍历完后再计算
    :param s:
    :return:
    '''
    lens = len(s)
    res = 0
    stack = []
    op = "+"  # 保留上一次运算符号
    tmp = 0
    for i in range(lens):
        if s[i].isdigit():
            tmp = tmp * 10 + int(s[i])
        if (not s[i].isdigit() and s[i] != " ") or i == lens - 1:
            if op == "+":
                stack.append(tmp)
            if op == "-":
                stack.append(-tmp)
            if op == "*" or op == "/":
                tmp = int(stack[-1] * tmp if op == "*" else stack[-1] / tmp)
                stack.pop()
                stack.append(tmp)

            tmp = 0
            op = s[i]
    while len(stack) != 0:
        res += stack.pop()
    return res


if __name__ == '__main__':
    print(calculate("14-3/2"))
