# -*- coding: UTF-8 -*-


def isSubsequence(s, t):
    '''
    392. 判断子序列（review）
    '''
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


def canJump(nums):
    '''
    55.跳跃游戏
    给定一个非负整数数组，你最初位于数组的第一个位置。

    数组中的每个元素代表你在该位置可以跳跃的最大长度。

    判断你是否能够到达最后一个位置。
    这个问题我们关心能够到达末尾（不要求刚好到达），只要最远能到达位置大于数组长度就可以
    不用关心剩余步数
    思路：如果当前所在位置<=当前能达到最大距离，并且当前索引+当前可走距离 > 当前能达到最大距离，就更相信最大距离。
    最后判断 最大距离+1（数组索引从0开始的） 是否比数组长度长
    '''
    # reach = 0
    # l = len(nums)
    # for i in range(l):
    #     if reach < i or reach >= l:
    #         break
    #     reach = max(reach, i + nums[i])
    # return reach >= l - 1
    max_len = 0
    for i, num in enumerate(nums):
        if i <= max_len and i + num > max_len:
            max_len = i + num
        else:
            break
    return True if max_len + 1 >= len(nums) else False


def canJumpTwo(nums):
    '''
    45. 跳跃游戏 II
    给定一个非负整数数组，你最初位于数组的第一个位置。

    数组中的每个元素代表你在该位置可以跳跃的最大长度。

    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    思路：遍历数组
    如果当前索引+当前能走的步数 > 数组长度，则步数+1 返回
    如果达不到，就比较索引i能达到的最大位置区间内，能达到的最远处

    :param nums:
    :return:
    '''
    step = 0
    over = len(nums) - 1
    idx = 0
    while idx < over:
        if idx + nums[idx] >= over:  # 如果当前位置能达到最远处 > 数组长度，则直接返回
            step += 1
            break
        max_pos = idx  # 记录当前达到的最远位置
        for i in range(idx + 1, idx + nums[idx] + 1):  # 贪心选择下一步走哪个位置能达到最远
            if nums[max_pos] + max_pos <= nums[i] + i:  # 如果下一步能达到的最远 比当前能达到的最远更优
                max_pos = i  # 记录最优值
        idx = max_pos  # 跟新最优下一步
        step += 1
    return step


def reconstructQueue(people):
    '''
    406. 根据身高重建队列(reverse)
    思路：先按H降序K升序 重排序原数组
    然后按K位置插入
    如果H小的人先排徐插入，那么他就受到没有排徐插入人的影响 ，有可能排在他的前面
    而贪心选择的思想是只关心已经排好序的，所以 应该先按身高从大到小排序
    这样 他在插入时候已经是最大的值考虑已经插入的，不用考虑剩下没插入的
    '''
    people = sorted(people, key=lambda i: (i[0], -i[1]), reverse=True)
    res = []
    for i in people:
        res.insert(i[1], i)
    return res


def leastInterval(tasks, n):
    '''
    621.任务调度器(review)
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
    :param tasks:
    :param n:
    :return:
    '''
    # dmap = {}
    # max_val = 0
    # for i in tasks:
    #     if dmap.get(i, -1) != -1:
    #         dmap[i] += 1
    #     else:
    #         dmap[i] = 1
    #     max_val = max(max_val, dmap[i])
    # count = 0
    # for v in dmap.values():
    #     if v == max_val:
    #         count += 1
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


def numRescueBoats(people, limit):
    '''
    881. 救生艇（review）
    第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

    每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

    返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
    思路

    如果最重的人可以与最轻的人共用一艘船，那么就这样安排。否则，最重的人无法与任何人配对，那么他们将自己独自乘一艘船。

    这么做的原因是，如果最轻的人可以与任何人配对，那么他们也可以与最重的人配对。
    :param people:
    :param limit:
    :return:
    '''
    people.sort()
    lo, hi = 0, len(people) - 1
    res = 0
    while lo <= hi:
        if (people[lo] + people[hi]) <= limit:
            lo += 1
            hi -= 1
        else:
            hi -= 1
        res += 1
    return res


def isMatch(s, p):
    '''
    TODO 多看看
     10.正则表达式匹配
    - 若p为空，若s也为空，返回true，反之返回false
    - 若p的长度为1，若s长度也为1，且相同或是p为'.'则返回true，反之返回false
    - 若p的第二个字符不为*，若此时s为空返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配
    - 若p的第二个字符为*，若s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母
    - 返回调用递归函数匹配s和去掉前两个字符的p的结果

    :param s:
    :param p:
    :return:
    '''
    if len(p) == 0:  # 如果p的长度为0，如果s的长度为0则匹配成功，否则匹配失败
        return len(s) == 0
    if len(p) == 1:  # 如果p的长度为1，如果s的长度也为1并且s[0]==p[0]或者p[0]=="." 则匹配成功，否则匹配失败
        return len(s) == 1 and (p[0] == s[0] or p[0] == ".")

    if p[1] != "*":  # 如果p的第一个字符不是"*" 如果s的长度为0则匹配失败，如果s,p第一个字符匹配成功，则继续匹配下一个字符
        if len(s) == 0:
            return False
        return (p[0] == s[0] or p[0] == ".") and isMatch(s[1:], p[1:])

    while len(s) != 0 and (s[0] == p[0] or p[0] == "."):  # 如果p的第一个字符是*，并且s的长度不为0，则尝试匹配第一个字符，成功了尝试匹配*后面的字符
        if isMatch(s, p[2:]):  # 匹配*后面的字符成功直接返回，失败了将s后移一位继续尝试匹配
            return True
        s = s[1:]
    return isMatch(s, p[2:])  # 如果s和p的第一个字符不匹配，则尝试匹配*后面的字符和s


def removeDuplicates(nums):
    '''
    26.删除排序数组中的重复项
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    思路：保存上一个，跟当前比较 一样就删除，不一样就更新上一个。
    注意的就是删除元素后长度减少 用while循环
    :param nums:
    :return:
    '''
    if len(nums) <= 1:
        return len(nums)
    tmp = nums[0]
    i = 1
    count = 1
    while count < len(nums):
        if nums[i] != tmp:
            i += 1
            count += 1
            tmp = nums[i]
        else:
            nums.remove(tmp)


def rotateOne(nums, k):
    '''
    review
    189.旋转数组
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    思路：元素的新位置在 (index+k) % 数组长度，但是这种情况需要空间复杂度为o（n）。
    :param nums:
    :param k:
    :return:
    '''
    lens = len(nums)
    r = [0 for i in range(lens)]
    for i in range(lens):
        index = (i + k) % lens
        r[index] = nums[i]

    nums = r


def rotate(nums, k):
    '''
    review
    189.旋转数组
    思路：原地解法
    k%len(nums)保证不溢出
    1.左边反转
    2.右边反转
    3.全部反转
    :param nums:
    :param k:
    :return:
    '''

    def reverse(left, right):
        while left < right:
            t = nums[left]
            nums[left] = nums[right]
            nums[right] = t
            left += 1
            right -= 1

    reverse(0, len(nums) - k % len(nums) - 1)
    reverse(len(nums) - k % len(nums), len(nums) - 1)
    reverse(0, len(nums) - 1)
    print(nums)


if __name__ == '__main__':
    print(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
