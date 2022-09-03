"""
problem:
        변수 이름
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""


testcases = int(input())
for i in range(testcases):
    name = input()
    ls = list(name)
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
            if ls[0] in (chr(65), chr(90)) or ls[0] in (chr(97), chr(122)) or ls[0] == chr(95):
                if ls[j] in (chr(65), chr(90)) or ls[j] in (chr(97), chr(122)) or ls[j] == chr(95):
                    print(1)
                    break
                else:
                    print(0)
                    break
            else:
                print(0)
                break