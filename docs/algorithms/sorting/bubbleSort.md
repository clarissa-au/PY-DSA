# bubbleSort.py

Bubblesort is (probably) the first sorting algorithm learned, and the first "real" algorithm that is in use learnt.
Super slow at O(n^2) speed, but it works and is easy to understand.

## Functions

```python
def bubbleSort(lst: list[float]) -> list[float]:
```

Sort the list using bubble sort.

## Example

```python
from pyDataStructAlgo import bubbleSort

NUMBERS = [4, 29, 57, 100, 3];
RESULT = bubbleSort(NUMBERS) # Returns [3, 4, 29, 57, 100]
```

## Tests

Testcases is provided in \test\algorithms\sorting\test_bubblesort.py. Use pytest to run it.
