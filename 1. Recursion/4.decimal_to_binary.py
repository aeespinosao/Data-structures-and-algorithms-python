def decimal_to_binary(number: int):
    if number == 0:
        return ""
    
    return decimal_to_binary(number//2) + f"{number%2}"


if __name__ == "__main__":
    print(decimal_to_binary(10))
    print(decimal_to_binary(13))