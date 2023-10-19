PI = None
PI_terms = None

def DSA_PI(terms:int=2500) -> float:
    if PI is not None and PI_terms > terms:
        return PI
    result = 3
    for i in range (0, terms):
        result = result + (-1)**i * 4 / (2*i+2) / (2*i+3) / (2*i+4)
    return result