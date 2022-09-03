import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    n = int(sys.stdin.readline())
    center = n // 2
    for y in range(n):
        for x in range(n):
            if max(abs(center - x), abs(center - y)) % 2 == 1:
                print(1, end="")
            else:
                print(0, end="")
        print()