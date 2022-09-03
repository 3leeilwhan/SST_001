import os
import queue

def get_subdir(path):
    try:
        dirfiles = os.listdir(path)
    except PermissionError:
        return

    subdir_list = []
    for each in dirfiles:
        full_name = path + each
        if os.path.isdir(full_name):
            subdir_list.append(full_name + "/")

    return subdir_list

dir_queue = queue.Queue()
dir_queue.put("C:/Users/3leei/AppData/Local/Continuum/anaconda3/")
all_dirs = []
while not dir_queue.empty():
    dir_name = dir_queue.get()
    all_dirs.append(dir_name)

    subdir_names = get_subdir(dir_name)
    for each in subdir_names:
        dir_queue.put(each)


cnt = 0
file_list = []
for i in all_dirs:

    file_list = os.listdir(i)

    for j in range(len(file_list)):
        if file_list[j].endswith(".py"):
            print(file_list[j])
            cnt += 1
for k in range(len(all_dirs)):
        if all_dirs[k].endswith(".py"):
            print(all_dirs[k])
            cnt += 1

print(cnt)