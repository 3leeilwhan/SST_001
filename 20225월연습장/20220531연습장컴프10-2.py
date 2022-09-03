def solution(nb, ln):
    if 0 < ln < 9:
        if nb < 3 or nb > 7:
            ln -= 1
        elif 4 <= nb <= 7:
            ln += 1


import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline())
    ls_numbers = list(map(int, sys.stdin.readline().split()))
    neighbors = 0
    for j in range(len(ls_numbers)):
        if j == 0:
            neighbors += ls_numbers[1]
            if 0 < ls_numbers[j] < 9:
                if neighbors < 3 or neighbors > 7:
                    ls_numbers[j] -= 1
                elif 4 <= neighbors <= 7:
                    ls_numbers[j] += 1

        elif j == len(ls_numbers)-1:
            neighbors += ls_numbers[-2]
            solution(neighbors, ls_numbers[j])
        else:
            neighbors += (ls_numbers[j-1] + ls_numbers[j+1])
            solution(neighbors, ls_numbers[j])
