# -*- coding: UTF-8 -*-
import sys


# 665. 非递减数列 
def deal(nums):
    i = -1
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            if i < 0:
                i = j
            else:
                return False
    if i in (-1, 0, len(nums) - 2):
        return True
    if nums[i + 1] >= nums[i - 1] or nums[i + 2] >= nums[i + 2]:
        return True
    return False


for line in sys.stdin:
    line = list(line)
    line = line[:-1]
    nums = []
    for i in line:
        if i != ' ':
            nums.append(int(i))

    if deal(nums):
        sys.stdout.write("YES")

    else:
        sys.stdout.write("NO")
