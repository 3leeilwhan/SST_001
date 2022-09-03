"""
problem:
        숫자의모든자리수반복곱하기
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""




testcases = int(input())
for i in range(testcases):
    n = input()
    ls = list(n)
    if len(ls) == 1:
        answer = int(n)
    else:
        while len(ls) > 1:

            while "0" in ls:
                ls.remove("0")
            answer = 1
            for k in range(len(ls)):
                answer *= int(ls[k])
            ls = list(str(answer))

    print(answer)