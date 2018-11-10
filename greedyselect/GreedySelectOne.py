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
    reach = 0  # 代表能达到的最远步数
    for i in range(len(nums)):  # 遍历数组
        if reach < i or reach >= len(nums):  # 如果当前位置比能达到的最远步数远的话，或者能达到最远步数 已经大于数组长度
            # 可以跳出循环
            break
        reach = max(reach, i + nums[i])  # 更新能达到的最远步数
    return reach >= len(nums) - 1


'''
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，
k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
每一次选择 下一个位置的时候值需要关心 站在前面的人就可以

'''


def comp(x1, x2):
    if x1[0] - x2[0] > 0:
        return 1
    elif x1[0] - x2[0] < 0:
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
    re = []
    compare = comp
    people.sort(cmp=compare, reverse=True)
    people.reverse()
    print(people)
    people.reverse()
    for i in people:
        re.insert(i[1], i)
    return re


'''
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。
思路：找出相同任务最多的假如是A共X个，这个任务在执行时之间必有n个间隔  可以用来运行其他服务。
    因为最后一组时间间隔不一定是满的  ，所以考虑 X-1 个  每个任务加上时间间隔 运行了 n+1个单位 X-1 * n+1 为 已经可以确定的
    那么中间的间隔就可以装下X-1 * 3个
    还剩下最边上一组这个时候 还需要考虑A因为还有一个A没计算 ，而且假如还有跟 相同任务最多的A 一样的任务假如B 那么 最边上
    一组还要有一个B ，总共就是（（X-1 ）* （n+1））+1（剩下一个A）+1（与A任务数量相同的B）但是 ，这时候剩下的其他任务 
    可以继续往之间的间隔之间添加，假如 添加到前面的间隔  之间已经添加满了
    就要在最边上哪组添加了。这是需要时间最长长度 已经超过刚才的计算值了  
    最大值现在是任务队列长度了 也就是len(tasks)
    所以最后要比较一下这两个值  取最大的
    
'''


def leastInterval(tasks, n):
    task = [0 for i in range(26)]
    for curTask in tasks:
        task[ord(curTask) - ord('A')] += 1  # 统计各个任务出现的次数
    task.sort(reverse=True)
    maxNum = task[0]  # 找出最长的那个任务
    count = 0  # 计算最边上应该放几个任务 （最大任务数的任务  总共有几个）
    for i in range(26):
        if task[i] == maxNum:
            count += 1
    # print(task)
    return max((maxNum - 1) * (n + 1) + count, len(tasks))  # 比较


'''
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
思路

如果最重的人可以与最轻的人共用一艘船，那么就这样安排。否则，最重的人无法与任何人配对，那么他们将自己独自乘一艘船。

这么做的原因是，如果最轻的人可以与任何人配对，那么他们也可以与最重的人配对。
'''


def numRescueBoats(people, limit):
    people.sort()
    count = 0
    i = 0
    j = len(people) - 1
    # print(people)
    while i <= j:
        count += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return count


def isMatch(s, p):
    if len(p) == 0:
        return len(s) == 0;
    if len(p) == 1:
        return len(s) == 1 and (p[0] == s[0] or p[0] == ".")

    if p[1] != "*":
        if len(s) == 0:
            return False
        return (p[0] == s[0] or p[0] == ".") and isMatch(s[1:], p[1:])
    f = isMatch
    while len(s) != 0 and (s[0] == p[0] or p[0] == "."):
        if f(s, p[2:]):
            return True
        s = s[1:]
    return isMatch(s, p[2:])


'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''


def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    tmp = nums[0]
    count = 1
    i = 1
    while i < len(nums):
        if nums[i] != tmp:
            tmp = nums[i]
            count += 1
            i += 1
        else:
            nums.remove(tmp)

    return count


def rotate(nums, k):
    lens = len(nums) - 2
    while k > 0:
        tmp = nums[len(nums) - 1]
        for i in range(lens + 1):
            nums[lens - i + 1] = nums[lens - i]
        nums[0] = tmp
        k -= 1


def rotateOne(nums, k):
    r=[]
    for i in nums:
        r.append(i)

    for i in range(len(nums)):
        if (i + k) >= len(nums):
            nums[(i + k) % len(nums)] = r[i]
        else:
            nums[(i + k)] = r[i]
    print(nums)


if __name__ == '__main__':
    print((rotateOne([1,2,3,4,5,6,7],
3)))
