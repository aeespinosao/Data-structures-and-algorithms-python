
class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
      
def find_node_in_tree(target, root):
    if not root:
        return False
    if target==root:
        return True
    
    return find_node_in_tree(target, root.left) or find_node_in_tree(target, root.right)

def findFirstCommonAncestor(n1, n2, root):
    n1_left = find_node_in_tree(n1, root.left)
    n2_left = find_node_in_tree(n2, root.left)
    
    if n1_left ^ n2_left:
        return root
    
    if n1_left:
        return findFirstCommonAncestor(n1, n2, root.left)
    
    return findFirstCommonAncestor(n1, n2, root.right)