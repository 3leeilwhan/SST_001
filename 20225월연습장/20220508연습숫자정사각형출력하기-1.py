testcases = int(input())
for i in range(testcases):
    n = int(input())

    for j in range(n):
        ls =[]
        for k in range(n):
            ls.append("0")

        for index, value in enumerate(ls[j:-j-1]):
            if value == "1":
                ls[index] = "0"
            elif value == "0":
                ls[index] = "1"


        result = "".join(ls)
        print(result)