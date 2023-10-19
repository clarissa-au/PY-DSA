# sqrt.py

Newton's method of finding the square root can be given by the following algorithm:

```markdown
    sqrt guess = number
    if number - sqrt guess ^ 2 > tolerance levels: //note the objective is number = sqrt^2
        sqrt guess = (sqrt guess + number/sqrt guess) / 2 //stepwise refine it until the above is true.
```

Note that this only works for nonnegative floats as input.

> Looking carefully, we see that the number of accurate digits approximately doubles on each
> iteration. This fantastic convergence rate means that we only need seven Newton iterations to
> obtain more than 60 accurate digits—the accuracy is quickly limited only by the precision of our
> floating-point numbers, a topic we will discuss in more detail later on.

(Square Roots via Newton’s Method, S. G. Johnson, MIT Course 18.335, <https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf>)

## Functions

```python
def newtonSqrt(val: float) -> float:
```

Return the square root of the inputted value to 10^-12 precision.

## Example

```python
from pyDataStructAlgo import newtonSqrt

NUMBER = 100;
RESULT = newtonSqrt(NUMBER) # Returns 10.0
```

## Tests

The test suite is avaliable at \test\algorithms\numerical\test_sqrt.py. Run it using pytests.
