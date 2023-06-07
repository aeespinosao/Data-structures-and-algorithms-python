class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight)>1:
        return -1
    
    return max(leftHeight, rightHeight) + 1

def isBalanced(root):
    return isBalancedHelper(root) > -1
    
