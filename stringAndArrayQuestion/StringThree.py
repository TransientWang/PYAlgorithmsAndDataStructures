# -*- coding: UTF-8 -*-

def minWindow(s, t):
    """
    76.最小窗口子字符串
    给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
    TODO 双指针是求解字符串问题的通用解法
    :param s:
    :param t:
    :return:
    """
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
            if hmap[ord(s[start])] == 0:  # 子串缩小到左边界为t中的字符为结束条件，让下次右边界能有t中的字符重新进入窗口当中
                count -= 1
            hmap[ord(s[start])] += 1  # 手指针遍历过得字符次数+1，还原（针对t中的字符）
            start += 1  # 手指针后移
    res = 0 if res == 2 ** 31 else res
    return s[cstart:cstart + res]


def calculate(s):
    '''
    227.基本计算器 II（review）
    实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
    思路：用栈来存储数字，由于涉及到优先级，所以遇到减号
    将后面的数字变成负值入栈，乘除法先计算，加减法遍历完后再计算，
    延迟计算，遇到符号再入栈

    :param s:
    :return:
    '''
    stack = []
    op = "+"
    tmp = 0
    for i, dig in enumerate(s):
        if dig.isdigit():
            tmp = tmp * 10 + int(dig)
        if not dig.isdigit() and dig != " " or i == len(s) - 1:  # 最后一个数也要入栈
            if op == "+":
                stack.append(tmp)
            elif op == "-":
                stack.append(-tmp)
            elif op == "/" or op == "*":
                t = stack.pop()
                tmp = t * tmp if op == "*" else int(t / tmp)
                stack.append(tmp)
            op = dig
            tmp = 0
    res = 0
    while stack:
        res += stack.pop()
    return res


def trapOne(height):
    pass


def trap(height):
    '''
    42.接雨水
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    思路：两次遍历，第一次从右到左，记录当前位置最高值，
    第二次从左到右从第二个点开始，比较水面高度（min(maxL, maxRs[i])延迟记录），存水量 =min(maxL, maxRs[i])= height[i]
    TODO 重新看
    :param height:
    :return:
    '''
    if height is None or len(height) <= 2:
        return 0
    maxR = [0 for i in range(len(height))]
    max_r = height[-1]
    max_l = height[0]
    res = 0

    for i in range(len(height) - 1, -1, -1):
        maxR[i] = max(max_r, height[i])
        max_r = max(max_r, maxR[i])

    for i in range(1, len(height)):
        max_l = max(max_l, height[i])
        res += max(min(max_l, maxR[i]) - height[i], 0)
    return res


def KMP(string, pattern):
    '''
    KMP算法
    :param string: 字符串
    :param pattern: 模式
    :return: 模式首字母在字符串中的位置
    '''
    next = [0 for i in range(len(pattern))]
    next[0] = -1

    def getNext():
        '''
        next[i] 表示pattern到前位置的子串的前缀与后相同的最远位置的后缀起始点。
        :return:
        '''
        j = 0
        k = -1
        while j < len(pattern) - 1:
            if k == -1 or pattern[j] == pattern[k]:
                j += 1
                k += 1
                if pattern[j] == pattern[k]:
                    next[j] = next[k]
                else:
                    next[j] = k
            else:  # 当匹配失败的时候string上的指针不用动，pattern上的指针需要回到与string 上i索引的位置的
                # 前一个索引位置开始向前匹配到pattern上从0到匹配失败索引位置的前一个索引为止的子串。
                # 这与个子串后缀相同的最长子串前缀的末尾索引位置。
                k = next[k]

    getNext()
    print(next)

    i, j = 0, 0
    while i < len(string) and j < len(pattern):
        if j == -1 or string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(pattern):
        return i - j
    else:
        return -1


def multiply(num1, num2):
    '''
    字符串相乘
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
    意思就是模拟一下数字相乘的过程，
    那吗就是用nums1的每一位分别与nums2相乘
    到下一位的时候乘完的结果后面还要加上索引位置数量的0
    然后保存起来
    都乘完后，就有了
    len(num1)个数字
    再把这些数字相加

    注意的地方就是，遇到相乘/相加大于10的数字进位的数要保存下来，append % 得出的数
    :param num1:
    :param num2:
    :return:
    '''
    if num1 == "0" or num2 == "0":
        return 0
    n1 = list(num1)
    n2 = list(num2)
    n1.reverse()
    n2.reverse()

    stack = []
    k = 0
    for i in n1:
        t = 0
        tmp = ""
        for j in n2:
            p = int(i) * int(j)
            p += t
            t = p // 10
            p %= 10
            tmp += str(p)
        if t != 0:
            tmp += str(t)

        tmps = list(tmp)

        tmps = ["0" for i in range(k)] + tmps
        k += 1
        stack.append(tmps)
    tmp = stack.pop()

    while len(stack) > 0:
        t = 0
        tmps = stack.pop()
        z = ""
        pos = 0
        while pos < max(len(tmps), len(tmp)):
            t1 = tmp[pos] if pos < len(tmp) else 0
            t2 = tmps[pos] if pos < len(tmps) else 0
            p = int(t1) + int(t2) + t
            t = p // 10
            p %= 10
            z += str(p)
            pos += 1
        if t != 0:
            z += str(t)
        z = list(z)
        tmp = z
    tmp = list(tmp)
    tmp.reverse()
    return "".join(tmp)


def shortestPalindrome(s):
    """
    214. 最短回文串(reveiw)
    最长回文前缀字符串是谁然后在它前面加上其后缀的逆序即可，即suff[::-1] + pref + suff
    :type s: str
    :rtype: str
    """
    # for i in range(len(s), -1, -1):
    #     pref, suff = s[:i], s[i:]
    #     if pref == pref[::-1]:
    #         return suff[::-1] + s
    # 优化
    # reversed_s = s[::-1]
    # for i in range(len(s)):
    #     if s.startswith(reversed_s[i:]):  # 说明s[:n-i]是回文
    #         return reversed_s[:i] + s
    # return s

    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1
    if i == len(s):
        return s
    tmp = s[i:][::-1]
    return tmp + shortestPalindrome(s[:i]) + s[i:]


if __name__ == '__main__':
    print(shortestPalindrome("2132-1"))
