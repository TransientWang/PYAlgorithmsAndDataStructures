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


def generateMatrix(n):
    """
    59. 螺旋矩阵 II
    思路：横向走完下一次横向步数 -1 ，纵向走完下一次纵向步数 -1
    定义四个方向 按 右→下→左→上 顺序遍历给数组赋值就可以
    :type n: int
    :rtype: List[List[int]]
    """
    direct = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 方向
    result = [[0 for i in range(n)] for i in range(n)]  # 输出数组
    weight = n  # 横向步数
    height = n - 1  # 纵向步数
    x = 0  # 坐标
    y = -1
    i = 1  # 赋值
    k = 0  # 方向辅助
    while n > 0:
        for h in range(weight):  # 横向
            x += direct[k % 4][0]
            y += direct[k % 4][1]
            result[x][y] = i
            i += 1
        k += 1
        weight -= 1
        for h in range(height):  # 纵向
            x += direct[k % 4][0]
            y += direct[k % 4][1]
            result[x][y] = i
            i += 1
        height -= 1
        k += 1
        n -= 1


def singleNumber(nums):
    """
    137. 只出现一次的数字 II
    https://cloud.tencent.com/developer/article/1131945
    :type nums: List[int]
    :rtype: int
    """
    a, b = 0, 0
    for num in nums:  # ^ 与 & 满足结合律     (1 ^ 3 ^4) = (1 ^ 4 ^3)
        a = (a ^ num) & ~b  # [2,2,2] 第三次的时候b 是 0 需要 异或 2 但是需要他为0
        # ，此时 a为2，a取反在 与就能 将 2再变成0
        b = (b ^ num) & ~a
    return a


def rangeBitwiseAnd(m, n):
    """
    201. 数字范围按位与
    基数与偶数按位与的最后一位一定是 （0&1) 0 ，
    那么在 m !=0 或者 m != n 的情况下（可以直接返回 m,0 & 其他 = 0，m &m =m），
    只需要从低位第二位起开（右移一位）始计算就可以，然后结果再相应的（左移回来）就可以。
    :type m: int
    :type n: int
    :rtype: int
    """
    count = 0
    while m != n and m != 0:
        m >>= 1
        n >>= 1
        count += 1
    return m << count
    # return m if (m == 0 or m == 0) else (rangeBitwiseAnd(m >> 1, n >> 1) << 1)


if __name__ == '__main__':
    print(rangeBitwiseAnd(8, 8))
