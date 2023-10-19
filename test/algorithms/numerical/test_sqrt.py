from pyDataStructAlgo import newtonSqrt
from pyDataStructAlgo import trunc

import pytest

def test_zeroSqrt():
    assert newtonSqrt(0) == 0

def test_negativeSqrt():
    with pytest.raises(ValueError, match='newtonSqrt input must be nonnegative.'):
        newtonSqrt(-2)

def test_pfSquareSqrt():
    assert newtonSqrt(100) == 10

def test_decimalSqrt():
    assert trunc(newtonSqrt(3.14), 12) == 1.772004514666

def test_Sqrt2():
    assert trunc(newtonSqrt(2), 12) == 1.414213562373