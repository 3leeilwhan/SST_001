"""
problem:
        두 구간이 차지하는 길이 구하기
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

import sys
testcases = int(input())
for i in range(testcases):
    ls = list(map(int, sys.stdin.readline().split()))
    if ls[0] <= ls[1] <= ls[2] <= ls[3]:
        print(0, end=" ")
        print((ls[1]-ls[0]) + (ls[3]-ls[2]))
    elif ls[0] <= ls[2] <= ls[1] <= ls[3]:
        print(ls[1]-ls[2], end=" ")
        print(ls[3]-ls[0])
    elif ls[0] <= ls[2] <= ls[3] <= ls[1]:
        print(ls[3]-ls[2], end=" ")
        print(ls[1]-ls[0])
    elif ls[2] <= ls[0] <= ls[1] <= ls[3]:
        print(ls[1]-ls[0], end=" ")
        print(ls[3]-ls[2])
    elif ls[2] <= ls[0] <= ls[3] <= ls[1]:
        print(ls[3]-ls[0], end=" ")
        print(ls[1]-ls[2])
    elif ls[2] <= ls[3] <= ls[0] <= ls[1]:
        print(0, end=" ")
        print((ls[1] - ls[0]) + (ls[3] - ls[2]))