def trunc(val:float, prec:int=0) -> float:
    val = float(int(val*10**(prec))/10**(prec))
    return val