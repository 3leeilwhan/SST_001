"""
problem:
        컴프10 -2
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


def solution(ln, nb, nl):
    if 0 < ln < 9:
        if nb < 3 or nb > 7:
            nl = ln - 1
        elif 4 <= nb <= 7:
            nl = ln + 1
    elif ln == 0:
        if 4 <= nb <= 7:
            nl = ln + 1
    elif ln == 9:
        if nb < 3 or nb > 7:
            nl = ln - 1
    return ln, nb, nl

import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    a, b = map(int, sys.stdin.readline().split())
    ls_numbers = list(map(int, sys.stdin.readline().split()))
    for h in range(b):
        new_ls = ls_numbers.copy()
        for j in range(len(ls_numbers)):
            neighbors = 0
            if j == 0:
                neighbors += ls_numbers[1]
                ls_numbers[j], neighbors, new_ls[j] = solution(ls_numbers[j], neighbors, new_ls[j])

            elif j == len(ls_numbers) - 1:
                neighbors += ls_numbers[-2]
                ls_numbers[j], neighbors, new_ls[j] = solution(ls_numbers[j], neighbors, new_ls[j])
            else:
                neighbors += (ls_numbers[j - 1] + ls_numbers[j + 1])
                ls_numbers[j], neighbors, new_ls[j] = solution(ls_numbers[j], neighbors, new_ls[j])

        ls_numbers = new_ls
    for l in new_ls:
        print(l, end=" ")
    print()