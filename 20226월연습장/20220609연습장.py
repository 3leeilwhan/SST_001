def search(list_, target, lower, upper):
    if lower > upper:
        return -1

    mid = (lower + upper) // 2
    if list_[mid] == 