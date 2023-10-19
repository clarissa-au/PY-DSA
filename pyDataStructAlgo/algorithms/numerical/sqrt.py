def newtonSqrt(val: float, prec:int=12) -> float:

    if val < 0:
        raise ValueError("newtonSqrt input must be nonnegative.")

    levelOfTolerance = 10**(-prec)
    sqrt = val

    while (abs(val - sqrt * sqrt)) > levelOfTolerance:

        sqrt = (sqrt + val / sqrt) / 2

    return sqrt