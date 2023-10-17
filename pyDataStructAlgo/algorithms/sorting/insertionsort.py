def insertionSort(lst: list[float]) -> list[float]:
    if len(lst) < 1:
        return lst
    ans = [lst.pop(0)]
    for i in lst:
        flag_inserted = False
        for j in range(0, len(ans)):
            if i < ans[j]:
                ans.insert(j, i)
                flag_inserted = True
                break
        if not flag_inserted:
            ans.append(i)
    return ans
