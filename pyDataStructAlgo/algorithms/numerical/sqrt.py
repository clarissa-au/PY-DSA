def newtonSqrt(val: float) -> float:

    if val < 0:
        raise ValueError("newtonSqrt input must be nonnegative.")

    levelOfTolerance = 10**(-12)
    sqrt = val

    while (abs(val - sqrt * sqrt)) > levelOfTolerance:

        sqrt = (sqrt + val / sqrt) / 2

    return sqrt