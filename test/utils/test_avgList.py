from pyDataStructAlgo import avgList

def test_avgList():
    assert avgList([1,2,3,4,5]) == 3

def test_avgNegativeList():
    assert avgList([-1,-4,-10]) == -5

def test_avgPNList():
    assert avgList([1,-1,2,-2,5]) == 1

def test_avgZeroList():
    assert avgList([0,0,0,0,0]) == 0

def test_emptyList():
    assert avgList([]) == 0