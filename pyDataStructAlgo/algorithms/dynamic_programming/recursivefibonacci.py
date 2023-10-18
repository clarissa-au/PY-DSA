fibonacciStorage = {}

def recursiveFibonacci(term: int) -> int:
    if term < 1:
        raise ValueError("recursiveFibonacci only support positive integer inputs!")
    if term == 1 or term == 2:
        return 1
    if str(term) in fibonacciStorage:
        return fibonacciStorage[str(term)]
    answer = recursiveFibonacci(term-1) + recursiveFibonacci(term-2)
    fibonacciStorage[str(term)] = answer
    return answer