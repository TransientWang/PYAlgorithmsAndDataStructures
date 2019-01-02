# -*- coding: UTF-8 -*-


def letterCombinations(digits):
    '''
    17.电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    思路：回溯法的本质是深度优先遍历（递归函数+终结条件）+剪枝函数
    DFS的结题思路就是在回溯函数中横向累积也就是for循环求出当前层的可能，然后递归，遇到终结条件
    或者剪枝函数时候结束该分支的遍历。

    :param digits:
    :return:
    '''
    number = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    if digits == "":
        return []
    res = []

    def backTrack(h, string):
        if h == len(digits):
            res.append(string)
            return
        for i, s in enumerate(number[int(digits[h])]):
            backTrack(h + 1, string + s)

    backTrack(0, "")
    return res


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]

    22.生成括号
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
    例如，给出 n = 3，生成结果为
    如果用 暴力法，我们需要省城2的N次方个组合，然后筛选出来
    回溯法：
    解法1：可以只在判断括号是否有效之后再继续添加括号
    如果 左括号 数量小于n 就可以添加一个左括号
    如果 右括号数量 小于n就可以继续添加一个右括号
    解法2：给生成的组合评分，左括号：1 右括号：-1
    搜索过程中小于0的组个直接停止。
    最后评分为0的加入结果集
    :param n:
    :return:
    """
    Parenth = ("(", ")")
    res = []

    # def generateBackTrack(tmp="", left=0, right=0):
    #     '''
    #
    #     :param tmp:
    #     :param left: 左括号的值
    #     :param right: 右括号的值
    #     :return:
    #     '''
    #     if len(tmp) == 2 * n:
    #         res.append(tmp)
    #         return
    #     if left < n:
    #         generateBackTrack(tmp + '(', left + 1, right)
    #     if right < left:
    #         generateBackTrack(tmp + ')', left, right + 1)

    def backTrack(h, tmp, score):
        '''
        :param h:DFS层数
        :param tmp:临时组合
        :param score:组合的评分，剪枝条件
        :return:
        '''
        if score < 0:  # 剪枝条件
            return
        if h == n * 2:  # 终结条件
            if score == 0:
                res.append(tmp)
            return

        for i in range(2):  # dfs过程
            backTrack(h + 1, tmp + Parenth[i], score + 1 if i == 0 else score - 1)

    backTrack(0, "", 0)
    return res


def partition(s):
    '''
    131.分割回文串
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回 s 所有可能的分割方案。
    思路:用一个index保存，当前遍历字符串的起始位置。然后从0开始，遇到回文串而且index==0说明刚开始分割，接下来的分割
    应该是跟它一组的，所以新创建一个列表，如果不是就将现在的回文串加入当前参数列表当中。
    如果index==len(s)则说明已经遍历完这个字符串了，可以将。参数列表加入结果集当中了。注意的是，它应该在 循环 外表，
    不然结果集会重复
    :param s:
    :return:
    '''
    pass
    res = []

    def isPalindrome(subSring):
        begin = 0
        end = len(subSring) - 1

        while begin < end:
            if subSring[begin] != subSring[end]:
                return False
            begin += 1
            end -= 1
        return True

    def find(result=[], index=0):
        if index == len(s):
            res.append(result)
        for i in range(index, len(s) + 1):
            if s[index:i] != "" and isPalindrome(s[index:i]):
                if index == 0:
                    find([s[index:i]], i)
                else:
                    find(result + [s[index:i]], i)

    find()
    return res


def removeInvalidParentheses(s):
    '''
    TODO 好好理解
    Remove Invalid Parentheses
    删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
    说明: 输入可能包含了除 ( 和 ) 以外的字符。
    解法I：深度优先搜索（DFS）+剪枝（Pruning）

利用评价函数计算字符串中未匹配括号的个数

尝试从输入字符串中移除括号，若得到的新字符串的失配括号比原字符串少，则继续搜索；

否则剪枝。
    :param s:
    :return:
    '''
    pass
    res = []
    mp = {"(": 1, ")": -1}

    def vaildate(subString):
        a = b = 0
        for i in subString:
            a += mp.get(i, 0)
            b += a < 0
            a = max(a, 0)
        return a + b

    def find(string):
        mins = vaildate(string)
        if mins == 0:
            res.append(string)
            return
        for i in range(len(string)):
            if string[i] in ["(", ")"]:
                tmp = string[:i] + string[i + 1:]
                if tmp not in visited and vaildate(tmp) < mins:
                    visited.add(tmp)
                    find(tmp)

    visited = set([s])
    find(s)
    return res if len(res) > 0 else [""]


if __name__ == '__main__':
    print(partition("aab"))
