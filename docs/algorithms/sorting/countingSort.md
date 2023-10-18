# countingsort.py

Counting Sort is a way to quickly sort large amounts of small positive datum.

## Functions

```python
def countingSort(lst: list[float]) -> list[float]:
```

Sort the list using counting sort.

## Example

```python
from pyDataStructAlgo import countingSort

NUMBERS = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
RESULT = countingSort(NUMBERS) # Returns  [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6]
```

## Tests

Testcases is provided in \test\algorithms\sorting\test_countingsort.py. Use pytest to run it.
