import sys
a, b, c = map(int, sys.stdin.readline().split())
mat = [[]]
small_mat = []
for y in range(a):
    for x in range(c):
        mat[y][x] = 0
print(mat)