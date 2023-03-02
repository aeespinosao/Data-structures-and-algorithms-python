
def power(base: int, exp: int):
    
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)

if __name__ == "__main__":
    print(power(2,1))
    print(power(2,4))
    print(power(3,3))
    print(power(1,50))
    print(power(4,-1))