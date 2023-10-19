from pyDataStructAlgo import ceil

def test_ceil0():
    assert ceil(0, 0) == 0

def test_ceil():
    assert ceil(152.3454, 3) == 152.346

def test_sameceil():
    assert ceil(53.2995, 4) == 53.2995

def test_ceilNeg():
    assert ceil(-45.2, 0) == -45

def test_ceilsDef():
    assert ceil(42.59) == 43