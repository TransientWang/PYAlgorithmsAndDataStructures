# -*- coding: UTF-8 -*-
'''
给定两个数组，编写一个函数来计算它们的交集。
'''


def singleNumber(nums):
    tmp = nums[0]
    index = 0
    left = 0
    right = 0

    while index < len(nums):
        if tmp == nums[index]:
            right = index
        elif right - left == 0:
            return nums[left]
        else:
            tmp = nums[index]
            left = index
            right = index
        index += 1
    return tmp


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] != nums2[j]:
            if nums1[i] < nums2[j] and i < len(nums1):
                i += 1
            elif nums1[i] > nums2[j] and j < len(nums2):
                j += 1
        else:
            if i > j:
                res.append(nums1[i])
            else:
                res.append(nums2[j])
            i += 1
            j += 1
    return res


'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''


def moveZeroes(nums):
    index = 1
    count = 0
    while index < len(nums):
        tmp = index
        while nums[tmp - 1] == 0:
            count += 0
            nums[tmp - 1] = nums[tmp]
            nums[tmp] = 0
            tmp -= 1
            if tmp == 0:
                break

        index += 1

    print(nums)


if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))
