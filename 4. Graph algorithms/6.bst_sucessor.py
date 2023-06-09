
class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node


def inOrderSuccessor(root, n):
    if n.right:
        return n.right
    parent = n.parent
        
    if parent.left is n:
        return parent
    return parent.parent
        

