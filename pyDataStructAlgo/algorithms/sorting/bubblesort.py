def bubbleSort(lst: list[float]) -> list[float]:
    pointer = 0
    for i in range(0,len(lst)):
        flag_sortCompleted = True
        for j in range(0, len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
                flag_sortCompleted = False
        if flag_sortCompleted:
            break;
    return lst