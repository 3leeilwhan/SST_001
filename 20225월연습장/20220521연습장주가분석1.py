"""
problem:
        주가 분석 -1
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

import sys
testcases = int(input())
for i in range(testcases):
    ls = list(map(int, sys.stdin.readline().split()))
    new_ls = []
    for j in range(len(ls)-1):
        if ls[j] != ls[j+1]:
            new_ls.append(ls[j])
    new_ls.append(ls[-1])

    cnt = 0
    for k in range(len(new_ls)-2):
        if (new_ls[k] < new_ls[k+1] and new_ls[k+2] < new_ls[k+1]):
            cnt += 1
    print(cnt)