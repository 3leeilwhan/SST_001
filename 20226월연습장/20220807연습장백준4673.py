list_ = []
for i in range(1, 10035):
    list_.append(i)

for j in range(1, 10035):
    answer = 0
    answer += j
    number = str(j)
    number = list(number)
    add_num = 0
    for k in range(len(number)):
        add_num += int(number[k])

    answer += add_num

    if answer in list_:
        list_.remove(answer)

for l in range(len(list_)):
    if list_[l] < 10000:
        print(list_[l])


