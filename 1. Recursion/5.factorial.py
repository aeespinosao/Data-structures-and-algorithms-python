
def factorial(number: int):
    if number == 1:
        return number
    return number * factorial(number-1)

if __name__ == "__main__":
    print(factorial(1))
    print(factorial(2))
    print(factorial(4))
    print(factorial(7))