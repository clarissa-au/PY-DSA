# insertionSort.py

Insertion Sort is (probably) the second sorting algorithm learned, and the second "real" algorithm that is in use learnt.
Same speed as Bubble Sort, but it works and is easy to understand.

## Functions

```python
def insertionSort(lst: list[float]) -> list[float]:
```

Sort the list using insertion sort.

## Example

```python
from pyDataStructAlgo import insertionSort

NUMBERS = [4, 29, 57, 100, 3];
RESULT = insertionSort(NUMBERS) # Returns [3, 4, 29, 57, 100]
```

## Tests

Testcases is provided in \test\algorithms\sorting\test_insertionsort.py. Use pytest to run it.
