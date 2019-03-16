# -*- coding: UTF-8 -*-
def reverseWords(s):
    """
    151. 翻转字符串里的单词
    :type s: str
    :rtype: str
    """
    p = list(filter(lambda x: x != "", s.split(" ")))
    p.reverse()
    return " ".join(p)


def compareVersion(version1, version2):
    """
    165. 比较版本号
    :type version1: str
    :type version2: str
    :rtype: int
    """

    def hmap(x):
        t = x.lstrip("0")
        return 0 if t == "" else int(t)

    t = list(map(hmap, version1.split(".")))
    k = list(map(hmap, version2.split(".")))
    j = 0
    for i in range(min(len(t), len(k))):
        if t[i] > k[i]:
            return 1
        elif t[i] < k[i]:
            return -1
        j = i
    if len(t) - len(k) != 0:
        if len(t) > len(k):
            if sum(t[j + 1:]) != 0: return 1
        else:
            if sum(k[j + 1:]) != 0: return -1

    return 0


def findRepeatedDnaSequences(s):
    """
    187. 重复的DNA序列
    :type s: str
    :rtype: List[str]
    """
    exist = set()
    res = []

    for i in range(len(s) - 9):

        if s[i:i + 10] in exist:
            res.append(s[i:i + 10])
        else:
            exist.add(s[i:i + 10])
    return res


def isIsomorphic(s, t):
    """
    205. 同构字符串
    相同的字符串必须被相同的字符替换
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    if len(set(s)) != len(set(t)):
        return False
    table = {}
    for i in range(len(s)):
        if s[i] in table and table[s[i]] != t[i]:
            return False
        else:
            table[s[i]] = t[i]
    return True


def numberToWords(num):
    """
    273. 整数转换英文表示
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "Zero"
    oneNum = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tenNum = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
              "Nineteen"]
    tyNum = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    Num = ["", "Thousand", "Million", "Billion"]
    num = str(num)

    t = []
    p = 0
    h = []
    for i in range(len(num) - 1, -1, -1):
        if p % 3 != 0 or p == 0:
            h.append(num[i])
        else:
            t.append(h[:])
            h = [num[i]]
        p += 1
    if h:
        t.append(h)
    res = ""
    for i in range(len(t)):
        z = ""
        for j in range(len(t[i])):
            if j == 0:
                z += " " + oneNum[int(t[i][j]) - 1]
            elif j == 1:
                m = int(t[i][j] + t[i][j - 1])
                if m > 9 and m < 20:
                    z = " " + tenNum[int(t[i][j - 1])]
                elif m > 19 and int(t[i][j - 1]) == 0:
                    z = " " + tyNum[int(t[i][j]) - 2]
                elif m > 19 and int(t[i][j - 1]) != 0:
                    z = " " + tyNum[int(t[i][j]) - 2] + z
            elif j == 2:
                if int(t[i][0]) + int(t[i][1]) == 0 and int(t[i][2]) != 0:
                    z = oneNum[int(t[i][j]) - 1] + " " + "Hundred"
                elif int(t[i][j]) != 0:
                    z = oneNum[int(t[i][j]) - 1] + " " + "Hundred" + z
                elif int(t[i][0]) + int(t[i][1]) == 0 + int(t[i][2]) == 0:
                    z = ""
        res = " " + z.strip() + " " + Num[i] + res if z != "" else res
    return res.strip()


def hIndex(citations):
    """
    274. H指数
    274. H指数II
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    # citations.reverse()
    # p = 0
    # for i in range(len(citations)):
    #     if i <= citations[i] - 1:
    #         p = i + 1
    # return p
    N = len(citations)
    low, high = 0, N - 1
    while low <= high:
        mid = (low + high) / 2
        if N - mid > citations[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return N - low


def addOperators(num, target):
    """
    282. 给表达式添加运算符（review）
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if not num or len(num) == 1 and int(num) != target:
        return []

    num = [int(i) for i in num]
    res = []
    #传统
    # def dfs(pos, path, cur, last):
    #     if cur == target and pos == len(num):
    #         res.append(path)
    #         return
    #     for i in range(pos, len(num)):
    #         cur_num = num[pos:i+1]
    #         if len(cur_num) > 1 and cur_num[0] == "0":
    #             break
    #         if pos == 0:
    #             dfs(i+1, cur_num, int(cur_num), int(cur_num))
    #         else:
    #             dfs(i + 1, path + "+" + cur_num, cur + int(cur_num), int(cur_num))
    #             dfs(i + 1, path + "-" + cur_num, cur - int(cur_num), -int(cur_num))
    #             dfs(i + 1, path + "*" + cur_num, cur - last + last * int(cur_num), last * int(cur_num))
    #
    # dfs(0, "", 0, 0)
    def dfs(i, expr, preSum, pre, cur):
        """
        :param i: 位置索引
        :param pre: 表达式中的最后一个数值参与计算所得到的结果
        :param preSum: 不包括 pre 的表达式结果
        :param expr: 结果表达式 ，其计算结果 = preSum + pre
        :param cur: 最后一次参与计算的一个数字 per/cur = 上
        :return:
        """
        if i == len(num) - 1:
            if preSum + pre + num[i] == target:
                res.append(expr + "+" + str(num[i]))
            if preSum + pre - num[i] == target:
                res.append(expr + "-" + str(num[i]))
            if preSum + pre * num[i] == target:
                res.append(expr + "*" + str(num[i]))
            # prevProd = pre/cur （prevProd 是最后一次参与计算的 pre。对于加减法来说prevProd 的值只值 ±1，
            # 对于乘法来说是最后一次次参与计算的pre）
            # curr*10+nums[i] 为前一个数与当前数字的和
            # new_prod = prevProd * (curr*10+nums[i]) = 10*prod + prod//curr*nums[i]
            if cur and 10 * pre + pre // cur * num[i] + preSum == target:  # 处理多个数字组合
                res.append(expr + str(num[i]))
        else:  #处理单个数组的情况
            dfs(i + 1, expr + "+" + str(num[i]), preSum + pre, num[i], num[i])
            dfs(i + 1, expr + "-" + str(num[i]), preSum + pre, -num[i], num[i])  # 因为计算的时候需要知道上一个参与计算的数值，
            # 但是如果考虑上一个参与计算的符号就会变得更加复杂，所以当有减号参与的时候，直接将计算数值变为负值
            dfs(i + 1, expr + "*" + str(num[i]), preSum, num[i] * pre, num[i])
            # if cur:
            # append nums[i] directly to last number, impossible when last number is 0
            if cur:  # 过滤最后一个参与计算的值为 0 的情况,处理多个数字的组合数
                dfs(i + 1, expr + str(num[i]), preSum, 10 * pre + pre // cur * num[i], cur * 10 + num[i])  # 处理多个数字组合

    dfs(1, str(num[0]), 0, num[0], num[0])
    return res


def wordPattern(pattern, str):
    """
    290. 单词模式
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    if len(pattern) == 1:
        return str != ""
    mp = dict()
    str = str.split(" ")
    if len(pattern) != len(str):
        return False
    for idx, i in enumerate(pattern):
        if mp.get(i, "#") == "#":
            for k, v in mp.items():
                if k != i and v == str[idx]:
                    return False
            mp[i] = str[idx]
        elif str[idx] != mp[i]:
            return False
    return True


def getHint(secret, guess):
    """
    299. 猜数字游戏（review）
    :type secret: str
    :type guess: str
    :rtype: str
    """
    secret = [i for i in secret]
    mp = []
    guess = [i for i in guess]
    A = 0
    B = 0
    for idx, i in enumerate(secret):
        if guess[idx] != i:
            mp.append(i)
    for idx, i in enumerate(secret):
        if guess[idx] == i:
            A += 1
        else:
            if guess[idx] in mp:
                mp.remove(guess[idx])
                B += 1
    return str(A) + "A" + str(B) + "B"
    #
    s = [0] * 10
    g = [0] * 10
    A = 0
    B = 0

    for i, v in enumerate(secret):
        if v == guess[i]:
            A += 1
        else:
            s[int(v)] += 1
            g[int(guess[i])] += 1
    for i in range(len(s)):
        B += min(s[i], g[i])
    return str(A) + "A" + str(B) + "B"


if __name__ == '__main__':
    print(addOperators("231",
                       22))
