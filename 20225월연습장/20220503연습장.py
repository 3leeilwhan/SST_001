import sys
testcases = int(input())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a in (1, 5, 6):
        print(a)
    elif a == 4:
        if b % 2 == 0:
            print(6)
        else:
            print(4)
    elif a == 9:
        if b % 2 == 0:
            print(1)
        else:
            print(9)
    elif a == 2:
        ls_2 = [6, 2, 4, 8]
        print(ls_2[b%4])
    elif a == 3:
        ls_3 = [1, 3, 9, 7]
        print(ls_3[b%4])
    elif a == 7:
        ls_7 = [1, 7, 9, 3]
        print(ls_7[b%4])
    elif a == 8:
        ls_8 = [6, 8, 4, 2]
        print(ls_8[b%4])
