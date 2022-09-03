testcases = int(input())
for i in range(testcases):
    n = int(input())

    for j in range(n):
        ls =[]
        for k in range(n):
            ls.append("0")

        if (0 < j < n//2):
            for l in range(j,-j-1):
                ls[l] = "1"





































        result = "".join(ls)
        print(result)