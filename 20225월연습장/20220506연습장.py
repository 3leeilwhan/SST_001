"""
problem:
        숫자정사각형출력하기-1
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

testcases = int(input())
for i in range(testcases):
    n = int(input())
    if n%4 == 3:
        for j in range(n):
            ls =[]
            if j == 0 or j == n-1:
                for k in range(j):
                    ls.append(1)
                    ls_new = [str(a) for a in ls]
                    print["".join(ls_new)]
            if








k = [1, 2, 3, 4, 5]
k_new =[str(a) for a in k]

print("".join(k_new))