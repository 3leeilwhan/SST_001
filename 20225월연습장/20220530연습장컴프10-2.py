import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

    for j in range(len(numbers)):
        if j == 0:
            neighbor = numbers[1]
        elif j == len(numbers)-1:
            neighbor = numbers[-2]
        else:
            neighbor = numbers[j-1] + numbers[j+1]

    for k in range(b):
        for j in range(len(numbers)):
            if neighbor <= 3:
                






