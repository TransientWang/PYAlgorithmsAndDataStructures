# -*- coding: UTF-8 -*-

def fractionToDecimal(numerator, denominator):
    '''
    166.分数化小数
    出现相同被除数就证明出现循环
    :param numerator:
    :param denominator:
    :return:
    '''
    if numerator == 0:
        return "0"
    bool = (numerator > 0) ^ (denominator > 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    dmap = {}
    result = numerator // denominator
    remainder = numerator % denominator
    result = str(result) if remainder == 0 else str(result) + "."
    index = len(result) - 1
    while remainder != 0:
        if remainder in dmap.keys():
            t = dmap[remainder] + 1
            result = result[:t] + "(" + result[t:] + ")"
            break
        else:
            dmap[remainder] = index
            index += 1
        remainder *= 10
        result += str((remainder // denominator))
        remainder = remainder % denominator
    return "-" + result if bool else result


def isPalindrome(x):
    '''
    回文数
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    :param x:
    :return:
    '''
    if x < 0:
        return False
    s = list(str(x))
    s.reverse()
    return x - int("".join(s)) == 0


def convert(s, numRows):
    """
    6. Z字形变换(新进度)
    思路:纵向观察，图形首先从0 行 增加到 numRows -1 ，然后在从 numRows -1 减少 到 0行 ，
    :type s: str
    :type numRows: int
    :rtype: str
    """

    if numRows == 1 or len(s) < numRows:
        return s
    res = [""] * numRows
    idx, step = 0, 1
    for i in s:
        res[idx] += i
        if idx == 0:
            step = 1
        elif idx == numRows - 1:
            step = -1
        idx += step
    return "".join(res)

def removeElement(nums, val):
    """
    27. 移除元素
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0

    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            nums.pop(i)
    return len(nums)

if __name__ == '__main__':
    print(removeElement([3,2,2,3], 3))
