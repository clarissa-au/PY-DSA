from pyDataStructAlgo import numericalFibonacci
from pyDataStructAlgo import trunc

import pytest

def test_baseCases():
    assert(round(numericalFibonacci(1))) == 1
    assert(round(numericalFibonacci(2))) == 1

def test_0():
    assert numericalFibonacci(0) == 0

def test_neg():
    assert round(numericalFibonacci(-2)) == -1

def test_decimal():
    neg2_5_Fibonacci = numericalFibonacci(-2.5)
    assert trunc(neg2_5_Fibonacci.real, 4) == 0.1342 and trunc(neg2_5_Fibonacci.imag, 4) == 1.4893
    

def test_bigFibonacci():
    assert(round(numericalFibonacci(50))) == 12586269025
