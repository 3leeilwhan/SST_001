from collections import Counter
import sys
testcases = int(sys.stdin.readline().strip())
books = []
for i in range(testcases):
    books.append(sys.stdin.readline().strip())

cnt = Counter(books)
cnt_list = cnt.most_common()

answer_list = []
answer_list.append(cnt_list[0][0])

for i in range(len(cnt_list)):
    if cnt_list[0][1] == cnt_list[i][1]:
        answer_list.append(cnt_list[i][0])
answer_list.sort()

print(answer_list[0])