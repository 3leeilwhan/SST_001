import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
list_B = list(str(B))
print(A * int(list_B[-1]))
print(A * int(list_B[-2]))
print(A * int(list_B[-3]))
print(A * B)