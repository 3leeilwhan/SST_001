t = int(input())
for i in range(t):
    a_, b_ = map(int, input().split())
    a = str(format(a_, 'b'))
    b = str(format(b_, 'b'))
    ls_a = list(format(a_, 'b'))
    ls_b = list(format(b_, 'b'))
    numa = 0
    numb = 0
    for x in range(len(ls_a)):
        if ls_a[x] == "1":
            numa += 1
    for y in range(len(ls_b)):
        if ls_b[y] == "1":
            numb += 1
    print(numa, numb, end=' ')
    if len(a) != len(b):
        c = abs(len(b) - len(a))
        cnt = 0
        if len(a) < len(b):
            answer = str(0) * c + a
            for k in range(len(answer)):
                if answer[k] != b[k]:
                    cnt += 1
        elif len(a) > len(b):
            answer = str(0) * c + b
            for k in range(len(answer)):
                if answer[k] != a[k]:
                    cnt += 1
        print(cnt)
    if len(a) == len(b):
        cnt_ = 0
        for j in range(len(a)):
            if a[j] != b[j]:
                cnt_ += 1
        print(cnt_)
