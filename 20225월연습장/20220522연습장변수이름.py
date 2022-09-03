testcases = int(input())
for i in range(testcases):
    n = input()
    ls = list(n)
    for j in range(len(ls)):
        if j != len(ls)-1:
            if ls[j] in (chr(0), chr(47)) or ls[j] in (chr(58), chr(64)) or ls[j] in (chr(91), chr(94)) or ls[j] == chr(96) or ls[j] in (chr(123), chr(127)):
                print(0)
                break
        else:
            if ls[0] in (chr(65), chr(90)) or ls[0] in (chr(97), chr(122)) or ls[0] == chr(95):
                print(1)

                break
            else:
                print(0)
                break