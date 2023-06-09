
class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    
    median = len(sortedArray)//2
    
    left = minimalTree(sortedArray[:median])
    right = minimalTree(sortedArray[median+1:])
    
    return BSTNode(sortedArray[median], left, right)