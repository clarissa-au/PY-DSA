# ceil.py

ceil.py ceiling a float to a specified number of decimals.

## Functions

```python
def ceil(val:float, prec:int=0) -> float:
```

Ceiling a float.

## Example

```python
from pyDataStructAlgo import ceil

NUMBER = 23.1;
RESULT = ceil(NUMBER) # Returns 24
```

## Tests

Testcases is provided in /test/utils/test_ceil.py. Use pytest to run it.
