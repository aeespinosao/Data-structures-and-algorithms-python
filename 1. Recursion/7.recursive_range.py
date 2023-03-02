def recursive_range(value: int):
    if value == 1:
        return value
    
    return value + recursive_range(value-1)

if __name__ == "__main__":
    print(recursive_range(6)) #21
    print(recursive_range(10)) #55