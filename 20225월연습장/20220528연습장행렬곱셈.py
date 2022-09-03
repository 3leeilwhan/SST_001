"""
problem:
        행렬 곱셈
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b, c = map(int, sys.stdin.readline().split())

    mat1 = []
    for j in range(a):
        mat1.append(list(map(int, sys.stdin.readline().split())))

    mat2 = []
    for j in range(b):
        mat2.append(list(map(int, sys.stdin.readline().split())))

    mat3 = []
    small_mat3 = []
    for x in range(c):
        small_mat3.append(0)
    for y in range(a):
        mat3.append(small_mat3)

    for x in range(a):
        for y in range(c):
            for k in range(b):
                mat3[x][y] += mat1[x][k] * mat2[k][y]
                if k == b-1:
                    print(mat3[x][y], end=" ")
                    mat3[x][y] = 0
        print()
