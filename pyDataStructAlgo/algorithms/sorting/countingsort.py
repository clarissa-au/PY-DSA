def countingSort(lst: list[float]) -> list[float]:
    max = 0
    for i in lst:
        if i < 0:
            raise ValueError("Counting Sort does not support negative numbers.")
        if i > max:
            max = i
    database = []
    for i in range(0, max+1):
        database.append(0)
    for i in lst:
        database[i] += 1
    ans = []
    for i in range(0, len(database)):
        for j in range(0, database[i]):
            ans.append(i)
    return ans
    