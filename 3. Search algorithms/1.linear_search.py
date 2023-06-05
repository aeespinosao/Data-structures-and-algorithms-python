def linear_search(array, value):
    for index, element in enumerate(array):
        if element==value:
            return index
    
    return -1