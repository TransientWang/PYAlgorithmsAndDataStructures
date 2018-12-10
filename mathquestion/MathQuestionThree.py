# -*- coding: UTF-8 -*-

def fractionToDecimal(numerator, denominator):
    '''
    分数化小数
    出现相同被除数就证明出现循环
    :param numerator:
    :param denominator:
    :return:
    '''
    if numerator == 0:
        return "0"
    symbol = 1 if numerator * denominator > 0 else -1  # 符号
    numerator = abs(numerator)
    denominator = abs(denominator)
    hmap = {}
    result = str(int(numerator / denominator))  # 整数部分
    remainder = numerator % denominator  # 余数，也是下一次计算的被除数
    if remainder != 0:
        result += "."
    index = len(result) - 1
    while remainder != 0:
        if hmap.get(remainder, -1) != -1:
            t = hmap.get(remainder) + 1
            result = result[:t] + "(" + result[t:] + ")"
            break
        else:
            hmap[remainder] = index
            index += 1

        remainder *= 10
        result += str(remainder // denominator)
        remainder = remainder % denominator
    if symbol < 0:
        result = "-" + result
    return result


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


if __name__ == '__main__':
    print(isPalindrome(-121))
