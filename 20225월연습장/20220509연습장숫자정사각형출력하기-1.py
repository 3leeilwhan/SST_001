testcases = int(input())
for i in range(testcases):
    n = int(input())
    for j in range(n):
        for k in range(n):
            if (j == k == n//2):
                print("0")

