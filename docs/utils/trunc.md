# trunc.py

trunc.py truncates a float to a specified number of decimals.

## Functions

```python
def trunc(val:float, prec:int=0) -> float:
```

Truncates a float.

## Example

```python
from pyDataStructAlgo import trunc

NUMBER = 23.1;
RESULT = trunc(NUMBER) # Returns 23
```

## Tests

Testcases is provided in /test/utils/test_trunc.py. Use pytest to run it.
