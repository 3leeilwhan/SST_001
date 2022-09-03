testcases = int(input())
for i in range(testcases):
    n = int(input())
    center = n // 2 + 1
    for y in range(1, n+1):
        for x in range(1, n+1):
            if x == y == center:
                print("*", end="")
            elif x == 1 or x == n:
                if y == 1 or y == n:
                    print("+", end="")
                else:
                    print("|", end="")
            elif y == 1 or y == n:
                print("-", end="")

            elif y == x:
                print("/", end="")
            elif y == n+1 - x:
                print("\\", end="")
            else:
                print(".", end="")
        print()