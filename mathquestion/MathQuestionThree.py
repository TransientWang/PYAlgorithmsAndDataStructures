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


if __name__ == '__main__':
    print(fractionToDecimal(2,3))
