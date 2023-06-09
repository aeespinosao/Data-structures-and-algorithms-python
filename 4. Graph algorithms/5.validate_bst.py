class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None
         
def isValidBST(root):
    if root is None:
        return True
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False
    
    return isValidBST(root.left) and isValidBST(root.right)
    