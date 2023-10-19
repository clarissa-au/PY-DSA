from pyDataStructAlgo import trunc

def test_trunc0():
    assert trunc(0, 0) == 0

def test_trunc():
    assert trunc(152.3454, 3) == 152.345

def test_sametrunc():
    assert trunc(53.2995, 4) == 53.2995

def test_truncNeg():
    assert trunc(-45.2, 0) == -45

def test_truncDef():
    assert trunc(42.59) == 42