# dynamicfibonacci.py

Recall that the Fibonacci Sequence is defined as

```markdown
    F(n) + F(n+1) = F(n+2)
    F(0) = 1
    F(1) = 1
```

Using this property, we can build a recursive Fibonacci function.

A traditional way of calculating Fibonacci function works from F(terms), then F(terms - 1), etc, down to F(1).
In Dynamic Programming, we reverse that by calculating F(1), F(2) and so on.
Threadwise the performance will be better than recursive Fibonacci, as one process is forked into 2 and then 4 for recursive case at the beginning while the dynamic one stays constant.

## Usage

```python
from pyDataStructAlgo import dynamicFibonacci

TERM = 300
F300 = dynamicFibonacci(300) # Returns 222232244629420445529739893461909967206666939096499764990979600
```

## Testing

**Warning: The values need to be computated is big! If you want to test using the default suite you must use a precomputated storage and not the naive method!**

The test suite is avaliable at \test\algorithms\dynamic_programming\test_dynamicfibonacci.py. Run it using pytests.
