"""
problem:
        빙고게임
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    mat = []
    for j in range(5):
        row = list(map(int, sys.stdin.readline().split()))
        mat.append(row)
    numbers = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for k in range(len(numbers)):
        cnt += 1
        talchool_k = False
        for y in range(len(mat)):
            talchool_y = False
            for x in range(len(mat[0])):

                if mat[x][y] == numbers[k]:
                    mat[x][y] = 0
                a_ = 0
                b_ = 0
                c_ = 0
                d_ = 0
                e_ = 0
                f_ = 0
                g_ = 0
                h_ = 0
                i_ = 0
                j_ = 0
                k_ = 0
                l_ = 0
                m_ = mat[0][0] + mat[0][4] + mat[4][0] + mat[4][4]
                for l in range(5):
                    a_ += mat[0][l]
                    b_ += mat[1][l]
                    c_ += mat[2][l]
                    d_ += mat[3][l]
                    e_ += mat[4][l]
                    f_ += mat[l][0]
                    g_ += mat[l][1]
                    h_ += mat[l][2]
                    i_ += mat[l][3]
                    j_ += mat[l][4]
                    k_ += mat[l][l]
                    l_ += mat[l][4-l]
                if a_ == 0 or b_ == 0 or c_ == 0 or d_ ==0 or e_ == 0 or f_ == 0 or g_ == 0 or h_ == 0 or i_ == 0 or j_ == 0 or k_ == 0 or l_ == 0 or m_ == 0:
                    talchool_k = True
                    talchool_y = True
                    break
            if talchool_y == True:
                break
        if talchool_k == True:
            break
    print(cnt)


