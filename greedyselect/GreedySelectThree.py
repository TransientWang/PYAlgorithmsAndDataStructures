# -*- coding: UTF-8 -*-
def fullJustify(words, maxWidth):
    """
    68. 文本左右对齐
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    idx = 0
    res = []
    while idx < len(words):
        count = len(words[idx])
        now_len = 1
        while idx + 1 < len(words) and count + len(words[idx + 1]) + 1 <= maxWidth:  # 贪心选择，找出能在一行放置的最大单词数
            count += len(words[idx + 1]) + 1
            now_len += 1
            idx += 1
        tmp = ""
        if idx != len(words) - 1 and now_len > 1:  # 单词数大于1 而且不是最后一行
            space = max(1, (maxWidth - count) // (now_len - 1) + 1)  # 求每个区间空格数量
            block = (maxWidth - count) % (now_len - 1) + (idx - now_len + 1)  # 求多余的空格应该分布在前几个区间
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " " * space
                if i < block:
                    tmp += " "
            tmp += words[idx]

        elif idx != len(words) - 1 and now_len == 1:  # 单词数等于 1 而且不是最后一行
            tmp = words[idx]
            tmp += " " * (maxWidth - count)
        else:  # 最后一行
            for i in range(idx - now_len + 1, idx):
                tmp += words[i]
                tmp += " "
            tmp += words[idx]
            tmp += " " * (maxWidth - len(tmp))
        res.append(tmp)
        idx += 1

    return res


import collections


def removeDuplicateLetters(s):
    """
    316. 去除重复字母
    :type s: str
    :rtype: str
    """
    map = dict()
    for i in s:
        if map.get(i, -1) == -1:
            map[i] = 1
        else:
            map[i] += 1
    res, cur_set = [], set()
    for i in s:
        if i not in cur_set:
            while res and res[-1] > i and map[res[-1]] > 0:
                cur_set.remove(res.pop())
            res.append(i)
            cur_set.add(i)
        map[i] -= 1
    return "".join(res)


def removeKdigits(num, k):
    """
    402. 移掉K位数字
    贪心选择
    :type num: str
    :type k: int
    :rtype: str
    """
    num = list(num)
    i = 0
    while i < len(num) - 1 and k > 0:
        if num[i] > num[i + 1] and k > 0:
            num.pop(i)
            k -= 1
            if i > 0:  # 重要：贪心选择退回到上一个，重新比较
                i -= 1
        else:
            i += 1
    num = num[:len(num) - k]
    while len(num) > 0 and num[0] == "0":
        num.pop(0)
    return "".join(num) if len(num) > 0 else "0"


def minPatches(nums, n):
    """
    330. 按要求补齐数组
    首先可以确定的是，
    nums中必然包含1，如果不包含1，那么[1,n]这个范围中的1就没法实现
    其次数组中的元素不能重复使用，如果允许重复使用，那么把1重复多次，就可以组成任意整数。
    令miss为[0,n]中缺少的最小整数，意味着我们可以实现[0,miss)范围内的任意整数。
    如果数组中有某个整数x<=miss, 那么我们可以把[0,miss)区间的所有整数加上x，区间变成了[x, miss+x)，由于区间[0,miss)和[x, miss+x)重叠，两个区间可以无缝连接起来，意味着我们可以把区间[0,miss)扩展到[0, miss+x)。
    如果数组中不存在小于或等于miss的元素，则区间[0,miss)和[x, miss+x) 脱节了，连不起来。此时我们需要添加一个数，最大限度的扩展区间[0, miss)。那添加哪个数呢？当然是添加miss本身，这样区间[0,miss)和[miss, miss+miss)恰好可以无缝拼接。
    举个例子，令nums=[1, 2, 4, 13, 43], n=100，我们需要让[1,100]内的数都能够组合出来。
    使用数字1,2,4，我们可以组合出[0, 8)内的所有数，但无法组合出8，由于下一个数是13，比8大，根据规则2，我们添加8，把区间从[0,8)扩展到[0,16)。
    下一个数是13，比16小，根据规则1，我们可以把区间从[0,16)扩展到[0,29)。

    下一个数是43，比29大，根据规则2，添加29，把区间从[0,29)扩大到[0,58)。

    由于43比58小，根据规则1，可以把区间从[0,58)扩展到[0,101)，刚好覆盖了[1,100]内的所有数。

    最终结果是添加2个数，8和29，就可以组合出[1,100]内的所有整数。
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    miss, count, i = 1, 0, 0
    while miss <= n:
        if i < len(nums) and miss >= nums[i]:
            miss += nums[i]
            i += 1
        else:
            miss <<= 1
            count += 1
    return count


if __name__ == '__main__':
    print(minPatches([1, 3],
                     6))
