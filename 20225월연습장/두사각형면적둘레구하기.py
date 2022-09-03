tast_case = int(input())
for i in range(tast_case):
    a_x1,a_y1,a_x2,a_y2 = map(int,input().split())
    b_x1,b_y1,b_x2,b_y2 = map(int,input().split())

    x_list = [a_x1,a_x2,b_x1,b_x2]
    y_list = [a_y1,a_y2,b_y1,b_y2]
    x_list.sort()
    y_list.sort()

    a_nurbi = (a_x2-a_x1)*(a_y2-a_y1)
    b_nurbi = (b_x2-b_x1)*(b_y2-b_y1)
    gyeopchim = 0
    result_giri = (a_x2-a_x1)+(b_x2-b_x1)+(a_y2-a_y1)+(b_y2-b_y1)

    if(a_x1<b_x1 and b_x1<a_x2)or(a_x1<b_x2 and b_x2<a_x2):
        if(a_y1<b_y1 and b_y1<a_y2)or(a_y1<b_y2 and b_y2<a_y2):
            gyeopchim = (x_list[2]-x_list[1])*(y_list[2]-y_list[1])
            result_giri = (x_list[3]-x_list[0])+(y_list[3]-y_list[0])
    result_nurbi = a_nurbi+b_nurbi-gyeopchim

    print(result_nurbi, result_giri*2)