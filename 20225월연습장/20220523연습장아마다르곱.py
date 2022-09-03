"""
problem:
        아마다르곱
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    b, a = map(int, sys.stdin.readline().split())
    map1 = []
    map2 = []
    for i in range(b):
        ls1 = list((map(int, sys.stdin.readline().split())))
        map1.append(ls1)

    for i in range(b):
        ls2 = list(map(int, sys.stdin.readline().split()))
        map2.append(ls2)

    map3 = map1
    for y in range(len(map1)):
        for x in range(len(map1[y])):
            map3[y][x] = map1[y][x] * map2[y][x]

    for y in range(len(map3)):
        for x in range(len(map3[y])):
            print(map3[y][x], end=" ")
        print()






