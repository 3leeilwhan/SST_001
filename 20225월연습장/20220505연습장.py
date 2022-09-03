"""
problem:
        정사각형 출력-3
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""



testcases = int(input())

for a in range(testcases):
    n = int(input())

    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n//2 or i == n-1):
                if (j == 0 or j == n//2 or j == n-1):
                    if (i == j and j == n//2):
                        print("*", end="")
                    else:
                        print("+", end="")
                else:
                    print("-", end="")

            elif (j == 0 or j == n//2 or j == n-1):
                print("|", end="")

            elif (i == j):
                print("\\", end="")
            elif (i == n-j-1):
                print("/", end="")
            else:
                print(".", end="")
        print("")
