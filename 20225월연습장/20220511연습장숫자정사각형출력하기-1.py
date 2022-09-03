tast_case = int(input())
for h in range(tast_case):
    n = int(input())
    mat = [[0 for i in range(n)]for i in range(n)]
    dot = n//2
    for i in range(dot,-1,-1):
        if i%2 != 0:
            for j in range(2*i+1):
                mat[dot-i][j+(dot-i)]=1
                mat[dot+i][j+(dot-i)]=1
                mat[j+(dot-i)][dot-i]=1
                mat[j+(dot-i)][dot+i]=1

    for i in range(n):
        for j in range(n):
            print(mat[i][j],end='')
        print()

