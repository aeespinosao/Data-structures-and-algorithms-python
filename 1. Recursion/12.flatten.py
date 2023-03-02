def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 

if __name__ == '__main__':
    print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
    print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
    print(flatten([[1], [2], [3]])) # [1, 2, 3]
    print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]
