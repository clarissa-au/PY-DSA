from pyDataStructAlgo import floor

def test_floor0():
    assert floor(0, 0) == 0

def test_floor():
    assert floor(152.3454, 3) == 152.345

def test_samefloor():
    assert floor(53.2995, 4) == 53.2995

def test_floorNeg():
    assert floor(-45.2, 0) == -46

def test_floorDef():
    assert floor(42.59) == 42