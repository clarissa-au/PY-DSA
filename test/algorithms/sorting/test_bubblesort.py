from pyDataStructAlgo import bubbleSort

def test_nullSort():
    assert bubbleSort([]) == []

def test_oneSort():
    assert bubbleSort([42]) == [42]

def test_Sort():
    assert bubbleSort([4, 29, 57, 100, 3]) == [3, 4, 29, 57, 100]

def test_zeroSort():
    assert bubbleSort([0,0,0,0]) == [0,0,0,0]

def test_SortedSort():
    assert bubbleSort([2, 24, 56, 79, 124]) == [2, 24, 56, 79, 124]

def test_negSort():
    assert bubbleSort([-4,-5,-29,-1, -158]) == [-158, -29, -5, -4, -1]

def test_PNSort():
    assert bubbleSort([-48, -76, 0, -2, 45]) == [-76, -48, -2, 0, 45]