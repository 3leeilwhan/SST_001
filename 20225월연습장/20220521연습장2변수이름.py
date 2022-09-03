testcases = int(input())
for i in range(testcases):
    name = input()
    ls = list(name)
    if ls[0] in (chr(0), chr(64)):
        print(0)
    elif ls[0] in (chr(91), chr(94)):
        print(0)
    elif ls[0] == chr(96):
        print(0)
    elif ls[0] in (chr(123), chr(127)):
        print(0)
    else:
        for j in range(len(ls)):
            if ls[j] in (chr(0), chr(47)):
                print(0)
                break
            elif ls[j] in (chr(58), chr(64)):
                print(0)
                break
            elif ls[j] in (chr(91), chr(94)):
                print(0)
                break
            elif ls[j] == chr(96):
                print(0)
                break
            elif ls[j] in (chr(123), chr(127)):
                print(0)
                break
            elif j == len(ls)-1:
                if ls[j] in (chr(48), chr(57)):
                    print(1)
                    break
                elif ls[j] in (chr(65), chr(90)):
                    print(1)
                    break
                elif ls[j] == chr(95):
                    print(1)
                    break
                elif ls[j] in (chr(97), chr(122)):
                    print(1)
                    break

