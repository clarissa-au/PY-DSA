def avgList(lst: list[float]) -> float:
    if len(lst) == 0:
        return 0
    from pyDataStructAlgo import sumList
    return sumList(lst)/len(lst)