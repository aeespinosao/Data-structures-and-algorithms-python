def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 

if __name__ == '__main__':
    print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']