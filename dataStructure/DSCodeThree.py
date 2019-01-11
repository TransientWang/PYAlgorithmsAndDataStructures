# -*- coding: UTF-8 -*-
def longestValidParentheses(s):
    """
    TODO 可以优化，合并两次循环，判断合法的同时判断最优值
    32. 最长有效括号
    思路：用一个栈 保存索引，遇到匹配的弹出
    然后遍历栈，找出间距最大的值
    :param s:
    :return:
    """
    stack = []
    for i in range(len(s)):
        if s[i] == ')':
            if stack and s[stack[-1]] == '(':  ## 这里要注意，不能想当然地用s[i-1]，因为我们有些下标直接continue了没有存到栈中去
                stack.pop()
                continue
        stack.append(i)

    max_length = 0
    next_index = len(s)
    while stack:
        cur_idx = stack.pop()
        cur_length = next_index - cur_idx - 1
        max_length = max(max_length, cur_length)
        next_index = cur_idx
    return max(next_index, max_length)


if __name__ == '__main__':
    print(longestValidParentheses(")()())"))
