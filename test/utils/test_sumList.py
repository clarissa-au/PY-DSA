from pyDataStructAlgo import sumList

def test_sumList():
    assert sumList([1,2,3,4,5]) == 15

def test_sumNegativeList():
    assert sumList([-1,-3,-10]) == -14

def test_sumPNList():
    assert sumList([1,-1,2,-2,3]) == 3

def test_sumZeroList():
    assert sumList([0,0,0,0,0]) == 0

def test_emptyList():
    assert sumList([]) == 0