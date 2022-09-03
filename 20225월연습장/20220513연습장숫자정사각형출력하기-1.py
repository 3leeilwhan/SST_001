"""
problem:
        숫자정사각형출력하기-1
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""



testcases = int(input())
for i in range(testcases):
    n = int(input())
    center = n // 2
    for y in range(n):
        for x in range(n):
            if max(abs(center - x), abs(center - y)) % 2 == 1:
                print(1, end="")
            else:
                print(0, end="")

        print()