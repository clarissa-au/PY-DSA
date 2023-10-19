from pyDataStructAlgo import recursiveFibonacci

import pytest

pytestmark = pytest.mark.timeout(5) # you will need to implement storage of already precomputed values; otherwise you will fail this test!

def test_baseCases():
    assert(recursiveFibonacci(1)) == 1
    assert(recursiveFibonacci(2)) == 1

def test_invalidInputs():
    with pytest.raises(ValueError, match='recursiveFibonacci only support positive integer inputs!'):
        recursiveFibonacci(0)
    with pytest.raises(ValueError, match='recursiveFibonacci only support positive integer inputs!'):
        recursiveFibonacci(-2)

def test_bigFibonacci():
    assert(recursiveFibonacci(50)) == 12586269025

def test_biggerFibonacci():
    assert(recursiveFibonacci(200)) == 280571172992510140037611932413038677189525

def test_biggererFibonacci():
    assert(recursiveFibonacci(300)) == 222232244629420445529739893461909967206666939096499764990979600
