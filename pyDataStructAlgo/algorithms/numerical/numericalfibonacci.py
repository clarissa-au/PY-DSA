def numericalFibonacci(val: complex) -> complex:
    from pyDataStructAlgo import DSA_PHI, newtonSqrt
    return (pow(DSA_PHI(), val) - pow((-1/DSA_PHI()), val))/(newtonSqrt(5))