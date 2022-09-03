import sys
testcases = int(input())
for i in range(testcases):
    n = list(map(int, sys.stdin.readline().split()))
    sum_ = sum(n) - n[0]
    avr = sum_ / n[0]
    for j in n[1:]:
        if j <= avr:
            n.remove(j)
    result = (len(n)-1) / n[0] * 100
    print("{:.3f}%".format(result))
