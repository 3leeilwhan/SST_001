import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline().split())
    mat1 = []
    mat2 = []
    for j in range(a):
        mat1.append(list(map(int, sys.stdin.readline().split())))
    for j in range(a):
        mat2.append(list(map(int, sys.stdin.readline().split())))
    for k 