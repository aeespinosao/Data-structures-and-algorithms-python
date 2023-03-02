
def sum_of_digits(number: int):
    
    if number == 0:
        return 0
    
    return number % 10 + sum_of_digits(number//10)

if __name__ == "__main__":
    
    print(sum_of_digits(4))
    print(sum_of_digits(10))
    print(sum_of_digits(123))
    print(sum_of_digits(11232))
    print(sum_of_digits(0))