# selectionsort.py

SelectionSort can be thought of as the inverse of insertion sort - in which it chooses the smallest element to append onto the answer array.

## Functions

```python
def selectionSort(lst: list[float]) -> list[float]:
```

Sort the list using selection sort.

## Example

```python
from pyDataStructAlgo import selectionSort

NUMBERS = [4, 29, 57, 100, 3];
RESULT = selectionSort(NUMBERS) # Returns [3, 4, 29, 57, 100]
```

## Tests

Testcases is provided in \test\algorithms\sorting\test_selectionsort.py. Use pytest to run it.
