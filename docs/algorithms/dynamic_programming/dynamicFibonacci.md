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

## Functions

```python
def dynamicFibonacci(term: int) -> int:
```

Return the term-th number in the Fibonacci Sequence.

## Usage

```python
from pyDataStructAlgo import dynamicFibonacci

TERM = 300
F300 = dynamicFibonacci(TERM) # Returns 222232244629420445529739893461909967206666939096499764990979600

LARGETERM = 1000
F1000 = dynamicFibonacci(LARGETERM) 
# Returns 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
```

## Testing

**Warning: The values need to be computated is big! If you want to test using the default suite you must use a precomputated storage and not the naive method!**

The test suite is avaliable at \test\algorithms\dynamic_programming\test_dynamicfibonacci.py. Run it using pytests.
