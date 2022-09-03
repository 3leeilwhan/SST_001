import sys
list_ = list(sys.stdin.readline().split())
N = int(list_[0])
K = int(list_[1])
number_list = []
for i in range(1, N+1):
    number_list.append(i)
plus = 0
result_list = []

for j in range(N):
    plus += K-1
    while plus >= len(number_list):
        plus -= len(number_list)

    result_number = number_list.pop(plus)
    result_list.append(result_number)

result_string = "<"
for k in range(len(result_list)-1):
    result_string = result_string + str(result_list[k]) + "," + " "

result_string += str(result_list[-1])
result_string += ">"
print(result_string)
