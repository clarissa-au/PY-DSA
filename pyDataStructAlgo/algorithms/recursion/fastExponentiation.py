def fastExp(base: float, exponent:int) -> float:
    if(exponent == 0):
        return 1
    if(exponent < 0):
        return fastExp(1/base, -exponent)
    if(exponent%2 == 0):
        return fastExp(base**2, exponent >> 1)
    return base * fastExp(base**2, exponent >> 1)