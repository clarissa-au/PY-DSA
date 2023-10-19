# pi.py

Using Nilakantha's series, which is shown here:

$\pi = 3 + \frac{4}{2 \times 3\times 4} - \frac{4}{4 \times 5\times 6}+ \frac{4}{6 \times 7\times 8} - \frac{4}{8 \times 9\times 10} \cdots $

We can estimate the value of Pi.

A global variable is coded so that memorization is possible if the called Pi is generated prior and has a higher or equal terms count.

## Functions

```python
def DSA_PI(terms:int=2500) -> float:
```

Using Nilakantha's series's n terms to estimate the value of Pi.

## Usage

```python
from pyDataStructAlgo import DSA_PHI

print(DSA_PI()) # 3.1415926535...
```
