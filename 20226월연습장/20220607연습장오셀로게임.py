"""
problem:
        오셀로 게임
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


import sys
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def isWall(x, y, color):
    global board
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return 0
    if not board[x][y]:
        return 0
    if board[x][y] == color:
        return 2
    return 1

def boardCheck(x, y, color):
    global board, dx, dy
    for i in range(8):
        nx = dx[i]
        ny = dy[i]
        change_list = []
        while True:
            a = isWall(x+nx, y+ny, color)
            if not a:
                break
            if a == 2:
                for c_x, c_y in change_list:
                    board[c_x][c_y] = color
                break
            if a == 1:
                change_list.append([x+nx, y+ny])
                nx += dx[i]
                ny += dy[i]

    board[x][y] = color

testcases = int(sys.stdin.readline())
for i in range(testcases):
    n = int(sys.stdin.readline())
    board = [[0]*8 for _ in range(8)]
    board[4][4] = 2
    board[3][3] = 2
    board[3][4] = 1
    board[4][3] = 1

    for n_ in range(n):
        x, y = map(int, sys.stdin.readline().split())

        if n_ % 2 == 0:
            color = 1
        else:
            color = 2
        boardCheck(x-1, y-1, color)

    w_count = 0
    b_count = 0
    for k in range(8):
        for l in range(8):
            if board[k][l] == 2:
                w_count += 1
                board[k][l] = "O"

            elif board[k][l] == 1:
                b_count += 1
                board[k][l] = "X"
            else:
                board[k][l] = "+"

    print(b_count, w_count)
    for k in range(8):
        for l in range(8):
            print(board[k][l], end=" ")
        print()
