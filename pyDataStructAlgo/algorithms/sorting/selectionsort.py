def selectionSort(lst: list[float]) -> list[float]:
    ans = []
    for i in range(0, len(lst)):
        min = float('inf')
        index = -1
        for j in range(0, len(lst)):
            if lst[j] < min:
                min = lst[j]
                index = j
        ans.append(min)
        lst.pop(index)
    return ans