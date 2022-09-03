n = input()
cnt = 0
answer = ""
new_n = n
if len(n) >= 2:
    while n != answer:
        ls = list(new_n)
        sum_ = 0
        for i in range(len(ls)):
            sum_ += int(ls[i])
        sum_ = str(sum_)

        answer = new_n[-1] + sum_[-1]
        new_n = answer
        cnt += 1


else:
    while "0" + n != answer:
        ls = list(new_n)
        sum_ = 0
        for i in range(len(ls)):
            sum_ += int(ls[i])
        sum_ = str(sum_)

        answer = new_n[-1] + sum_[-1]
        new_n = answer
        cnt += 1

print(cnt)