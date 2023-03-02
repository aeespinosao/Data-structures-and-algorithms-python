def product_of_array(array: list):
    if len(array) == 1:
        return array[0]
    
    return array[0] * product_of_array(array[1:])

if __name__ == "__main__":
    print(product_of_array([1,2,3])) #6
    print(product_of_array([1,2,3,10])) #60