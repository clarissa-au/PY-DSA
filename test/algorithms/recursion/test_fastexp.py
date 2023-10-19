from pyDataStructAlgo import fastExp

def test_0base():
    assert fastExp(0, 5) == 0

def test_0to0():
    assert fastExp(0, 0) == 1

def test_normal():
    assert fastExp(10, 3) == 1000

def test_evenNormal():
    assert fastExp(2, 4) == 16

def test_bigExpo():
    assert fastExp(2, 10**3) == 2**1000