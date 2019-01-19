# -*- coding: UTF-8 -*-
def simplifyPath(path):
    """
    71. 简化路径
    思路：用栈处理问题 。
    将文件夹名 压入栈中
    :type path: str
    :rtype: str
    """
    path += "/"
    fd = ""  # 存储文件夹 和 ".\.."
    res = ""
    stack = []

    for i in path:
        if i == "/" and fd == "..":
            if stack:
                stack.pop()
            fd = ""
            continue
        elif i == "/" and fd == ".":
            fd = ""
            continue
        elif i == "/":
            if fd != "":
                stack.append(fd)
            fd = ""
            continue
        fd += i

    if not stack:
        return "/"
    while stack:
        res = res + "/" + stack.pop(0)

    return res


def removeDuplicates(nums):
    """
    80.删除排序数组中的重复项 II
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    while idx < len(nums):
        if idx < 2 or nums[idx] != nums[idx - 2]:
            idx += 1
        else:
            nums.pop(idx)
    return idx


def grayCode(n):
    """
    89. 格雷编码

    关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);
    如 n = 3:
    G(0) = 000,
    G(1) = 1 ^ 0 = 001 ^ 000 = 001
    G(2) = 2 ^ 1 = 010 ^ 001 = 011
    G(3) = 3 ^ 1 = 011 ^ 001 = 010
    G(4) = 4 ^ 2 = 100 ^ 010 = 110
    G(5) = 5 ^ 2 = 101 ^ 010 = 111
    G(6) = 6 ^ 3 = 110 ^ 011 = 101
    G(7) = 7 ^ 3 = 111 ^ 011 = 100
    每一位是 i 与 i 右移一位的异或结果
    :type n: int
    :rtype: List[int]
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == '__main__':
    print(simplifyPath("/home//foo/"))
