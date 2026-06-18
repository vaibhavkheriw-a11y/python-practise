# Write a Python program to get the Fibonacci series between 0 to 50.

def fibonacci(toNum):
    first = 0
    second = 1
    now = 0
    fibonacciSeries = []

    while first <= toNum:
        fibonacciSeries.append(first)
        now = first + second
        first = second
        second = now

    return fibonacciSeries

print(f"Fibonacci series is {fibonacci(50)}")