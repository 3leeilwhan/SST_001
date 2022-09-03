import sys
testcases = int(input())
for i in range(testcases):
    name, enter_leave = map(str, sys.stdin.readline().split())
    ls = []
    if enter_leave == "enter":
        ls.append(name)
    if enter_leave == "leave":
        ls.remove(name)
for j in range(len(ls)):
    print(ls[j])
