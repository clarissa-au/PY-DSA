fibonacciStorage = {}

def recursiveFibonacci(term: int) -> int:
    if term < 1:
        raise ValueError("recursiveFibonacci only support positive integer inputs!")
    answer = recursiveFibonacci_logic(term)
    fibonacciStorage.clear()
    return answer

def recursiveFibonacci_logic(term: int) -> int:
    if term == 1 or term == 2:
        return 1
    if str(term) in fibonacciStorage:
        return fibonacciStorage[str(term)]
    answer = recursiveFibonacci_logic(term-1) + recursiveFibonacci_logic(term-2)
    fibonacciStorage[str(term)] = answer
    return answer