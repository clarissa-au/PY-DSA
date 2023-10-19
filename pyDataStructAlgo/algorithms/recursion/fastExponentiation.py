def fastExp(base: float, exponent:int) -> float:
    if(exponent == 0):
        return 1
    elif(exponent < 0):
        return fastExp(1/base, -exponent)
    elif(exponent%2 == 0):
        return fastExp(base**2, exponent >> 1)
    else:
        return base * fastExp(base**2, exponent >> 1)