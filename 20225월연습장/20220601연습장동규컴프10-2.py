tast_case = int(input())
for case in range(tast_case):
    n,k = map(int,input().split())
    mat = list(map(int,input().split()))
    for j in range(k):
        mat_imsi = mat[:]
        for i in range(len(mat)):
            cnt = 0
            if i == 0:
                cnt += mat[i+1]
            elif i == len(mat)-1:
                cnt += mat[i-1]
            else:
                cnt += mat[i-1] + mat[i+1]

            if cnt < 3 or 7 < cnt:
                if mat_imsi[i] > 0:
                    mat_imsi[i] -= 1
            elif 4 <= cnt <= 7:
                if mat_imsi[i] < 9:
                    mat_imsi[i] += 1

        mat = mat_imsi
    for i in mat:
        print(i,end = ' ')
    print()