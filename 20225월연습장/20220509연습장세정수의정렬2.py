"""
problem:
        세 정수의 정렬2
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


import sys
testcases = int(input())
for i in range(testcases):
    a, b, c = map(int, sys.stdin.readline().split())

    if (a <= b) == True:
        if (b <= c) == True:
            print(a, b, c)
        else:
            if (a <= c) == True:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if (c <= b) == True:
            print(c, b, a)
        else:
            if (a <= c) == True:
                print(b, a, c)
            else:
                print(b, c, a)
