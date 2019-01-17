# -*- coding: UTF-8 -*-
def searchInsert(nums, target):
    """
    35. 搜索插入位置
    思路：二分搜索
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # for i in range(len(nums)):
    #     if target == nums[i]:
    #         return i
    #     elif target < nums[i]:
    #         return i
    # return len(nums)

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


def searchMatrix(matrix, target):
    """
    74. 搜索二维矩阵
    思路：二分搜索的变种
    先从最左边的列中二分，找到target所在的行，然后在该行中二分搜索target
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
        return False
    row = len(matrix)
    col = len(matrix[0]) if row else 0
    left, right = 0, row - 1
    while left <= right:
        mid_row = left + ((right - left) >> 2)
        if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
            m, n = 0, col - 1
            while m <= n:
                mid_col = m + ((n - m) // 2)
                if matrix[mid_row][mid_col] > target:
                    n = mid_col - 1
                elif matrix[mid_row][mid_col] < target:
                    m = mid_col + 1
                else:
                    return True
            return False  # 找不到就没有
        elif target < matrix[mid_row][0]:
            right = mid_row - 1
        else:
            left = mid_row + 1
    return False


if __name__ == '__main__':
    searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
                 13)
