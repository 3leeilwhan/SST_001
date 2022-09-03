"""
problem:
        컴프10 -2
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

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
                #solution(neighbors, ls_numbers[j])
                if 0 < ls_numbers[j] < 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1
                    elif 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 0:
                    if 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1

            elif j == len(ls_numbers) - 1:
                neighbors += ls_numbers[-2]
                #solution(neighbors, ls_numbers[j])
                if 0 < ls_numbers[j] < 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1
                    elif 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 0:
                    if 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1
            else:
                neighbors += (ls_numbers[j - 1] + ls_numbers[j + 1])
                #solution(neighbors, ls_numbers[j])
                if 0 < ls_numbers[j] < 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1
                    elif 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 0:
                    if 4 <= neighbors <= 7:
                        new_ls[j] = ls_numbers[j] + 1
                elif ls_numbers[j] == 9:
                    if neighbors < 3 or neighbors > 7:
                        new_ls[j] = ls_numbers[j] - 1
        ls_numbers = new_ls
    for l in new_ls:
        print(l, end=" ")
    print()