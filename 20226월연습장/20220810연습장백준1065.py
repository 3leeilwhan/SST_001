import sys
number = int(sys.stdin.readline())
if number < 100:
    print(number)
else:
    result = 99
    for i in range(100, number + 1):
        ls_i = list(str(i))
        if int(ls_i[0]) - int(ls_i[1]) == int(ls_i[1]) - int(ls_i[2]) or int(ls_i[2]) - int(ls_i[1]) == int(ls_i[1]) - int(ls_i[0]):
            result += 1

    print(result)
