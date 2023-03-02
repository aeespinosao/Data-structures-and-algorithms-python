def common_divisor(a: int, b: int):
    if b == 0:
        return a
    
    return common_divisor(b, a%b)

if __name__ == "__main__":
    print(common_divisor(8,12))
    print(common_divisor(48,18))