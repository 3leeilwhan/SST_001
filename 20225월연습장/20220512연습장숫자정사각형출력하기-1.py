testcases = int(input())
for i in range(testcases):
    n = int(input())

    center = n//2

    for j in range(n):
        ls =[]
        for k in range(n):
            ls.append("0")
    for k in range(center, -1, -1):
        if k % 2 != 0:
            for l in range(2*k+1):
                ls[center - k][l + (center - k)] = 1
                ls[center + k][center + (center - k)] = 1
                ls[l + (center - k)][center - k] = 1
                ls[l + (center - k)][center + k] = 1

    for i in range(n):
        for j in range(n):
            print(ls[i][j],end='')
        print()

