# numericalFibonacci.py

Using the Binet Formula, which is given below;

$\frac{(\phi)^n - (\frac{-1}{\phi})^n}{\sqrt{5}}$

it is possible to find out terms not normally accessible by algorithms.

Note that phi is given in DSA_PHI() and sqrt() is given by newtonSqrt(). Due to precision limits from newtonSqrt(), the answer is only accurate at most up to 1 in 10^-12.

## Functions

```python
def numericalFibonacci(val: complex) -> complex:
```

Returns Binet Formula(val), which can be one approximation for nonexistent fibonacci numbers.

## Usage

```python
from pyDataStructAlgo import numericalFibonacci

neg_2_th_FibonacciNum = numericalFibonacci(-2)
print(neg_2_th_FibonacciNum) # ~= -1
```

## Testing

The test suite is avaliable at \test\algorithms\numerical\test_numericalfibonacci.py. Run it using pytests.
