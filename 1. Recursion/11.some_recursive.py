def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 1:
        return cb(arr[0])
    
    return cb(arr[0]) or someRecursive(arr[1:], cb)

if __name__ == '__main__':
    print(someRecursive([1,2,3,4], isOdd)) # true
    print(someRecursive([4,6,8,9], isOdd)) # true
    print(someRecursive([4,6,8], isOdd)) # false