from pyDataStructAlgo import dynamicFibonacci

import pytest

def test_baseCases():
    assert(dynamicFibonacci(1)) == 1
    assert(dynamicFibonacci(2)) == 1

def test_invalidInputs():
    with pytest.raises(ValueError, match='dynamicFibonacci only support positive integer inputs!'):
        dynamicFibonacci(0)
    with pytest.raises(ValueError, match='dynamicFibonacci only support positive integer inputs!'):
        dynamicFibonacci(-2)

def test_bigFibonacci():
    assert(dynamicFibonacci(50)) == 12586269025

def test_biggerFibonacci():
    assert(dynamicFibonacci(200)) == 280571172992510140037611932413038677189525

def test_biggererFibonacci():
    assert(dynamicFibonacci(300)) == 222232244629420445529739893461909967206666939096499764990979600
