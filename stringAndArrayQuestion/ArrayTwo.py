# -*- coding: UTF-8 -*-

def gameOfLife(board):
    '''
    生命游戏
    状态转换
    0 死细胞到死细胞
    1 活细胞到活细胞
    2 或细胞到死细胞
    3 死细胞到活细胞
    :param board:
    :return:
    '''
    vectorx = (1, -1, 0, 0, 1, 1, -1, -1)  # 八个方向向量
    vectory = (0, 0, 1, -1, 1, -1, 1, -1)

    row = len(board)
    colum = len(board[0])
    for i in range(row):
        for j in range(colum):
            count = 0
            for v in range(8):
                x = i + vectorx[v]
                y = j + vectory[v]
                if x >= 0 and x < row and y >= 0 and y < colum and (board[x][y] == 1 or board[x][y] == 2):
                    count += 1
            if board[i][j] and (count < 2 or count > 3):
                board[i][j] = 2
            elif not board[i][j] and count == 3:
                board[i][j] = 3
    for i in range(row):
        for j in range(colum):
            board[i][j] %= 2

    for i in range(row):
        print(board[i])





if __name__ == '__main__':
    print()
