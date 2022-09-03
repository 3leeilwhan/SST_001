testcases = int(input())
for i in range(testcases):
    n = input()
    ls = [n]
    while len(ls) > 1:

        for j in ls:
            ls.remove("0")
        answer = 1
        for k in range(len(ls)):
            answer *= str(int(ls[k]))
        for l in range(len(answer)):
            ls.append(answer)
        if len(ls) == 1:
            break



