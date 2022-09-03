import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b, c = map(int, sys.stdin.readline().split())

    mat1 = []
    for j in range(a):
        mat1.append(list(map(int, sys.stdin.readline().split())))
    print(mat1)

    mat2 = []
    for j in range(b):
        mat2.append(list(map(int, sys.stdin.readline().split())))
    print(mat2)

    mat3 = []
    small_mat3 = []
    for x in range(c):
        small_mat3.append(0)
    for y in range(a):
        mat3.append(small_mat3)
    print(mat3)

