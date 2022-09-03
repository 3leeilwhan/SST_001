"""
problem:
        해밍 거리
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline().split())
    a = list(format(a, "b"))
    b = list(format(b, "b"))
    cnt_a = 0
    for j in range(len(a)):
        if a[j] == "1":
            cnt_a += 1
    print(cnt_a, end=" ")
    cnt_b = 0
    for j in range(len(b)):
        if b[j] == "1":
            cnt_b += 1
    print(cnt_b, end=" ")
    cnt_ab = 0
    a.reverse()
    b.reverse()
    abs_ = abs(len(a) - len(b))
    if len(a) > len(b):
        for k in range(abs_):
            b.append("0")
    else:
        for k in range(abs_):
            a.append("0")

    for l in range(len(a)):
        if a[l] != b[l]:
            cnt_ab += 1

    print(cnt_ab)

