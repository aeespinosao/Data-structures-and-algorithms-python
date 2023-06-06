
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    


def treeToLinkedList(tree, custDict = {}, d = 1):
    print(tree)
    if d not in custDict:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
    
    if tree.left is not None:
        treeToLinkedList(tree.left, custDict, d+1)
    if tree.right is not None:
        treeToLinkedList(tree.right, custDict, d+1)
    
    return custDict



