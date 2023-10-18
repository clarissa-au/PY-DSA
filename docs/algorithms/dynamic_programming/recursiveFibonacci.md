# recursivefibonacci.py

Recall that the Fibonacci Sequence is defined as

```markdown
    F(n) + F(n+1) = F(n+2)
    F(0) = 1
    F(1) = 1
```
 
Using this property, we can build a recursive Fibonacci function.

## Usage

```python
from pyDataStructAlgo import recursiveFibonacci

TERM = 300
F300 = recursiveFibonacci(300) # Returns 222232244629420445529739893461909967206666939096499764990979600
```

## Testing

** Warning: The values need to be computated is big! If you want to test using the default suite you must use a precomputated storage and not the naive method!**

The test suite is avaliable at \test\algorithms\dynamic_programming\test_recursivefibonacci.py. Run it using pytests.
