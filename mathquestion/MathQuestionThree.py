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


def computeArea(A, B, C, D, E, F, G, H):
    """
    223. 矩形面积
    :type A: int
    :rtype: int
    """
    return (C - A) * (D - B) + (H - F) * (G - E) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)


def isNumber(s):
    """
    65. 有效数字
    :type s: str
    :rtype: bool
    """

    def isInt(s):
        if s == '': return False
        if s[0] in ['+', '-']:
            s = s[1:]
        if s == '': return False
        for c in s:
            if c > '9' or c < '0':
                return False
        return True

    def isFloat(s):
        if s == '': return False
        if s[0] in ['+', '-']:
            s = s[1:]
        if s == '': return False
        if s == '.':
            return False
        if s.count('.') > 1:
            return False
        for c in s:
            if c == '.' or '0' <= c <= '9':
                continue
            else:
                return False
        return True

    s = s.strip()

    if len(s) == 0: return False
    data = s.split('e')
    if len(data) > 2:
        return False
    elif len(data) == 2:
        return isFloat(data[0]) and isInt(data[1])
    else:
        return isFloat(data[0])


def calculate(s):
    """
    224. 基本计算器
    :type s: str
    :rtype: int
    """

    def total(stack):
        while len(stack) > 2:
            if stack[1] == '+':
                p = stack[0] + stack[2]
            else:
                p = stack[0] - stack[2]
            stack = stack[3:]
            stack.insert(0, p)
        return stack

    stack = []
    k = ""
    for idx, i in enumerate(s):
        if i == " ":
            continue
        if i == "(":
            stack.append([])

        elif str(i).isnumeric():
            k += str(i)
            if idx < len(s) - 1 and str(s[idx + 1]).isnumeric():
                continue
            if len(stack) > 0 and isinstance(stack[-1], list):
                stack[-1].append(int(k))
            else:
                stack.append(int(k))
            k = ""
        elif i == "+" or i == "-":
            if isinstance(stack[-1], list):
                stack[-1].append(i)
            else:
                stack.append(i)
        elif i == ")":
            p = stack.pop()
            if not isinstance(p, list):
                p = [p]
            else:
                p = total(p)
            if len(stack) > 0 and isinstance(stack[-1], list):
                stack[-1] += p
            else:
                stack += p
    stack = total(stack)

    return stack[0]


def calculate_(s):
    """
    224. 基本计算器
    :type s: str
    :rtype: int
    """
    num = 0
    result = 0
    operator = 1
    stack = []
    for char in s:
        if char == '+':
            result += operator * num
            num = 0
            operator = 1
        elif char == '-':
            result += operator * num
            num = 0
            operator = -1
        elif char == '(':
            stack.append(result)  # 把“(”前的结果和操作符保存起来
            stack.append(operator)
            num = 0
            result = 0
            operator = 1
        elif char == ')':
            result += operator * num  # 这个result是()中计算的结果
            num = 0
            result = result * stack.pop()
            result += stack.pop()
        elif char != ' ':
            num = num * 10 + int(char)
    result += operator * num
    return result


if __name__ == '__main__':
    print(calculate_("(1+(4+5+2)-3)+(6+8)"))
