"""
problem:
        변수 이름
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

testcases = int(input())
for i in range(testcases):
    n = input()
    ls = list(n)
    ls_copy = list(n)
    if n.isalnum() == True:
        if ls[0].isnumeric() == True:
            print(0)
        else:
            print(1)

    elif "_" in ls:
        while "_" in ls:
            ls.remove("_")
        new_n = "".join(ls)
        if ls == []:
            print(1)

        elif new_n.isalnum() == True:
            if ls_copy[0].isnumeric() == True:
                print(0)
            else:
                print(1)
        else:
            print(0)
    else:
        print(0)