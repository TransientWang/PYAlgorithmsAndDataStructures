# -*- coding: UTF-8 -*-
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
'''


def isSubsequence(s, t):
    lens = len(s)
    if lens == 0:
        return True
    i = 0
    for j in t:
        if s[i] == j:
            i += 1
            if i == len(s):
                return True
    return False


'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
这个问题我们关心能够到达末尾（不要求刚好到达），只要最远能到达位置大于数组长度就可以
不用关心剩余步数
'''


def canJump(nums):
    reach = 0 #代表能达到的最远步数
    for i in range(len(nums)):             #遍历数组
        if reach < i or reach >= len(nums): #如果当前位置比能达到的最远步数远的话，或者能达到最远步数 已经大于数组长度
                                            #可以跳出循环
            break
        reach = max(reach, i + nums[i])      #更新能达到的最远步数
    return reach >= len(nums) - 1


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4]))
