from pyDataStructAlgo import countingSort

import pytest

def test_nullSort():
    assert countingSort([]) == []

def test_oneSort():
    assert countingSort([42]) == [42]

def test_Sort():
    assert countingSort([4, 29, 57, 100, 3]) == [3, 4, 29, 57, 100]

def test_zeroSort():
    assert countingSort([0,0,0,0]) == [0,0,0,0]

def test_SortedSort():
    assert countingSort([1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 2, 3, 3, 4, 4, 5]

def test_aLotOfSmallNumbers():
    assert countingSort([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]) == [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6]

def test_negSortRaiseError():
    with pytest.raises(ValueError, match='Counting Sort does not support negative numbers.'):
        countingSort([-4,-5,-29,-1, -158])
