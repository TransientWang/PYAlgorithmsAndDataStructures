# -*- coding: UTF-8 -*-
import sys
# if __name__ == '__main__':
#
# for line in sys.stdin:
#     #     a = line
#     #     a = 1024  - int(a)
#     amount = 1
#     coins = [1, 4, 16, 64]
#
#     dp = [2**31 for _ in range(amount + 1)]  # 兑换 i 元的方案数
#     dp[0] = 0
#
#
#     for j in range(1, amount + 1):
#         for i in coins:
#             if j >=i:
#
#                 dp[j] = min(dp[j-i] +1,dp[j])
#
#     print(dp[-1])

# if __name__ == '__main__':
#     import sys
#
#     if __name__ == "__main__":
#         # 读取第一行的n
#         n = int(sys.stdin.readline().strip())
#         ans = 0
#         for i in range(n):
#
#             line = sys.stdin.readline().strip()
#             stack = []
#             for i, val in enumerate(line):
#
#                 if len(stack) > 1:
#                     if val == stack[-1] and val == stack[-2]:
#                         stack.pop(-2)
#                 if len(stack) > 3:
#                     if val == stack[-1] and stack[-2] == stack[-3]:
#                         stack.pop(-1)
#                 stack.append(val)
#             print("".join(stack))

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for x in range(n):
#         lens = int(sys.stdin.readline().strip())+2
#         ratings = list(map(lambda a:int(a),sys.stdin.readline().strip().split()))
#         ratings = ratings + [ratings[0]]
#         ratings = [ratings[-2]] + ratings
#         lens = len(ratings)
#         r = [1 for i in range(lens)]
#
#         for x in range(1, lens):
#             r[x] = r[x - 1] + 1 if ratings[x] > ratings[x - 1] and r[x] <= r[x - 1] else r[x]
#
#         t = lens - 1
#         for x in range(1, lens):
#             r[t - x] = r[lens - x] + 1 if ratings[t - x] > ratings[lens - x] and r[t - x] <= r[lens - x] else r[t - x]
#
#         sum = 0
#
#         for q in r:
#             sum += q
#         sum -= r[0]
#         sum -= r[-1]
#         print(sum)

# def gameOfLife(board):
#     """
#     :type board: List[List[int]]
#     :rtype: void Do not return anything, modify board in-place instead.
#     """
#     vector = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
#     for x in range(len(board)):
#         for y in range(len(board[0])):
#             count = 0
#             for vx, vy in vector:
#                 aimx = x + vx
#                 aimy = y + vy
#                 if aimx < 0 or aimx >= len(board) or aimy < 0 or aimy >= len(board[0]):
#                     continue
#                 if board[aimx][aimy] == 1 or board[aimx][aimy] == 2:
#                     count += 1
#             if (count < 2 or count > 3) and (board[x][y] == 1):
#                 board[x][y] = 2  # 死亡
#             elif count == 3 and board[x][y] == 0:
#                 board[x][y] = 3
#     for x in range(len(board)):
#         for y in range(len(board[0])):
#             board[x][y] %= 2
import sys

if __name__ == "__main__":
    # 读取第一行的n
    def findL(values, idx, target):
        if idx < len(values):
            l = r = True
            if idx * 2 + 1 < len(values) and values[idx * 2 + 1] > target:
                return False
            elif idx * 2 + 1 < len(values):
                l = findL(values, idx * 2 + 1, target)
            if idx * 2 + 2 < len(values) and values[idx * 2 + 1] > target:
                return False
            elif idx * 2 + 2 < len(values):
                r = findL(values, idx * 2 + 1, target)
            if l and r:
                return True
            return False
        else:
            return True


    def findR(values, idx, target):
        if idx < len(values):
            l = r = True
            if idx * 2 + 1 < len(values) and values[idx * 2 + 1] <= target:
                return False
            elif idx * 2 + 1 < len(values):
                l = findL(values, idx * 2 + 1, target)
            if idx * 2 + 2 < len(values) and values[idx * 2 + 1] <= target:
                return False
            elif idx * 2 + 2 < len(values):
                r = findL(values, idx * 2 + 1, target)
            if l and r:
                return True
            return False
        else:
            return True


    for i in range(1):
        # 读取每一行
        line = sys.stdin.readline().strip()
        p = None

        if len(line) == 0:
            print(False)
        else:
            if len(line) > 1:
                p = line.split(",")
            values = list(map(lambda a: int(a), p))
            # print(values)
            # 把每一行的数字分隔后转化成int列表

            for v in range(1, (len(values) - 1) // 2):
                if values[v] <= values[v * 2 + 1] or values[v] >= values[v * 2 + 2] or not findL(values, v * 2 + 1,
                                                                                                 values[
                                                                                                     v]) or not findR(
                    values, v * 2 + 2, values[v]):
                    print(False)
                    break
            print(True)

            left = []

    # for i in range(1):
    #     # 读取每一行
    #
    #     values = list(map(lambda a: int(a), sys.stdin.readline().strip().split(" ")))
    #     mx = values[0]
    #     my = values[1]
    #     k = values[2]
    #     dp = [[0 for _ in range(my)] for _ in range(mx)]
    #
    #     res = [0]
    #
    #     if len(dp) == 1:
    #         print()
    #
    #     def find(x, y, k, dp):
    #         if x >= 0 and x < mx and y >= 0 and y < my:
    #             dp[x][y] = 1
    #             res[0] += 1
    #             vector = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    #             for vx, vy in vector:
    #                 nx = x + vx
    #                 ny = y + vy
    #                 if nx >= 0 and nx < mx and ny >= 0 and ny < my and nx + ny <= k and dp[nx][ny] != 1:
    #                     find(nx, ny, k, dp)
    #
    #
    #     find(0, 0, k, dp)
    #     print(res[0])
    # for i in range(1):
    #     # 读取每一行
    #     values = sys.stdin.readline().strip()
    #     res = 0
    #
    #     i = int(values)
    #     while True:
    #         if i == 1:
    #             res += 1
    #             break
    #         elif i == 0:
    #             break
    #         x = i % 2
    #         print(x)
    #         if x == 1:
    #             res += 1
    #         i = i // 2
    #     print(res)
