import sys
testcases = int(sys.stdin.readline())
list_ = [0] * 10000
for i in range(testcases):
    number = int(sys.stdin.readline())
    list_[number-1] += 1

for j in range(len(list_)):
    if list_[j] > 0:
        for k in range(list_[j]):
            print(j+1)


