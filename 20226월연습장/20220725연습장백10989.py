import sys
testcases = int(sys.stdin.readline())
list_ = [0] * 10000000
number_list = []
for i in range(testcases):
    number = int(sys.stdin.readline())
    number_list.append(number)
    list_[number] = number


for i in range(1, len(number_list)+1):
    thing = 0
    for j in range(len(number_list)):
        if number_list[j] == i:
            thing += 1
    for k in range(len(list_)):
        if list_[k] > 0:
            for l in range(thing):
                print(list_[k])
