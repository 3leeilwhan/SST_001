import sys
testcases = int(sys.stdin.readline())
for i in range(testcases):
    list_ = list(sys.stdin.readline().split())

    sum_score = 0
    for j in range(1, len(list_)):
        sum_score += int(list_[j])

    average = sum_score / int(list_[0])

    list_.remove(list_[0])

    number = 0
    for k in range(len(list_)):
        if int(list_[k]) > average:
            number += 1

    higher_average_percentage = number / len(list_) * 100

    print("{:.3f}%".format(higher_average_percentage))
