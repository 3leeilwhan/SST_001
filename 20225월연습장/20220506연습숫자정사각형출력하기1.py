"""
problem:
        숫자정사각형출력하기-1
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

testcases = int(input())
for a in range(testcases):
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            if n&4 == 3:
                for k in range(n):
                    if i % 2 == 1 or j % 2 == 1:
                        print("1", end="")
                    elif i % 2 != 1 or j % 2 != 1:
                        print("0", end="")
            elif n%4 != 3:
                for k in range(n):
                    if i % 2 == 1 or j % 2 == 1:
                        print("0", end="")
                    elif i % 2 != 1 or j % 2 != 1:
                        print("1", end="")
        print("")






