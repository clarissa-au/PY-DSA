# floor.py

floor.py floors a float to a specified number of decimals.

## Functions

```python
def floor(val:float, prec:int=0) -> float:
```

Flooring a float.

## Example

```python
from pyDataStructAlgo import floor

NUMBER = 23.1;
RESULT = floor(NUMBER) # Returns 23
```

## Tests

Testcases is provided in /test/utils/test_floor.py. Use pytest to run it.
