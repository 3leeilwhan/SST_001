"""
problem:
        두 사각형 면적 둘레 구하기
        국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20213048 이일환
"""

testcases = int(input())
for i in range(testcases):
    x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
    x1_2, y1_2, x2_2, y2_2 = map(int, input().split())
    ls_x = [x1_1, x2_1, x1_2, x2_2]
    ls_y = [y1_1, y2_1, y1_2, y2_2]
    area_1 = (x2_1 - x1_1) * (y2_1 - y1_1)
    area_2 = (x2_2 - x1_2) * (y2_2 - y1_2)
    ls_x.sort()
    ls_y.sort()
    length_1_2 = (ls_x[3] - ls_x[0]) * 2 + (ls_y[3] - ls_y[0]) * 2

    if (x2_1 <= x1_2) or (x2_2 <= x1_1) or (y2_1 <= y1_2) or (y2_2 <= y1_1):
        print(area_1 + area_2, end=" ")
        print((x2_1 - x1_1) * 2 + (y2_1 - y1_1) * 2 + (x2_2 - x1_2) * 2 + (y2_2 - y1_2) * 2)
    else:
        print(area_1 + area_2 - (ls_x[2] - ls_x[1]) * (ls_y[2] - ls_y[1]), end=" ")
        print(length_1_2)

