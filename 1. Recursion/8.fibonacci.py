def fib(value: int):
    if value <= 1:
        return value
    
    return fib(value-1) + fib(value-2)

if __name__ == "__main__":
    print(fib(4)) #3
    print(fib(10)) #55
    print(fib(28)) #317811
    print(fib(35)) #9227465