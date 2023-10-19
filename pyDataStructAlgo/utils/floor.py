def floor(val:float, prec:int=0) -> float:
    from pyDataStructAlgo import trunc
    if trunc(val, prec) != val:
        if val >= 0:
            val = float(int(val*10**(prec))/10**(prec))
        else:
            val = float(int(val*10**(prec)-1)/10**(prec))
    return val