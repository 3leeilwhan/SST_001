t = int(input())
for i in range(t):
    a, k = (map(int,input().split()))
    n = list(map(int,input().split()))
    for x in range(k):
        new_n = n[:]
        for j in range(len(n)):
            if j == 0:
                if n[1] < 3 or 7 < n[1]:
                    if n[0] == 0:
                        new_n[0] = n[0]
                    else:
                        new_n[0] = n[0] - 1
                elif 3 < n[1] <= 7:
                    if n[0] == 9:
                        new_n[0] = n[0]
                    else:
                        new_n[0] = n[0] + 1

            elif j == len(n) - 1:
                if n[-2] < 3 or 7 < n[-2]:
                    if n[-1] == 0:
                        new_n[-1] = n[-1]
                    else:
                        new_n[-1] = n[-1] - 1
                elif 3 < n[-2] <= 7:
                    if n[-1] == 9:
                        new_n[-1] = n[-1]
                    else:
                        new_n[-1] = n[-1] + 1
            else:
                neighbors = n[j - 1] + n[j + 1]
                if neighbors < 3 or 7 < neighbors:
                    if n[j] == 0:
                        new_n[j] = n[j]
                    else:
                        new_n[j] = n[j] - 1
                elif 3 < neighbors <= 7:
                    if n[j] == 9:
                        new_n[j] = n[j]
                    else:
                        new_n[j] = n[j] + 1

        n = new_n
    for l in new_n:
        print(l, end=" ")
    print()

