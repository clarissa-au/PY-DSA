def dynamicFibonacci(term: int) -> int:
    if term < 1:
        raise ValueError("dynamicFibonacci only support positive integer inputs!")
    fibonacciStorage = {'1' : 1, '2': 1}
    if term <= 2:
        return 1
    for i in range(3, term+1):
        fibonacciStorage[str(i)] = fibonacciStorage[str(i-1)] + fibonacciStorage[str(i-2)]
        fibonacciStorage.pop(str(i-2))
    return fibonacciStorage[str(i)]