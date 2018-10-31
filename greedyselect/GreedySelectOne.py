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
'''
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，
k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
每一次选择 下一个位置的时候值需要关心 站在前面的人就可以

'''
def comp(x1,x2):

    if x1[0] -x2[0] > 0:
        return 1
    elif x1[0] -x2[0] < 0:
        return -1
    else:
        return x2[1] - x1[1]

'''
思路：先按H降序K升序 重排序原数组
然后按K位置插入
如果H小的人先排徐插入，那么他就受到没有排徐插入人的影响 ，有可能排在他的前面
而贪心选择的思想是只关心已经排好序的，所以 应该先按身高从大到小排序
这样 他在插入时候已经是最大的值考虑已经插入的，不用考虑剩下没插入的
'''
def reconstructQueue(people):
    re =[]
    compare = comp
    people.sort(cmp = compare,reverse=True)
    people.reverse()
    print(people)
    people.reverse()
    for i in people:
        re.insert(i[1],i)
    return re
if __name__ == '__main__':
    print(reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))

