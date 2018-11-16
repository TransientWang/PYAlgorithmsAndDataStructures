# -*- coding: UTF-8 -*-
def productExceptSelf(nums):
    '''
    给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    :param nums:
    :return:
    '''
    r = [1 for i in range(len(nums))]
    r1 = [1 for i in range(len(nums))]
    res = [1 for i in range(len(nums))]

    for i in range(len(nums) - 1):
        r[i + 1] = nums[i] * r[i] if i >= 0 else nums[i]

    for i in range(1, len(nums)):
        r1[i] = nums[-i] * r1[i - 1] if i >= 0 else nums[-i]

    r1.reverse()

    for i in range(len(nums)):
        res[i] = r[i] * r1[i]
    return res


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
