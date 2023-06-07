
class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
      
def first_common_ancestor(node1, node2):
  search1, search2 = node1, node2
  ancestors1, ancestors2 = [], []
  while search1 or search2:
    if search1:
      if search1 in ancestors2:
        return search1
      ancestors1.append(search1)
      search1 = search1.parent
      print(ancestors1)
    if search2:
      if search2 in ancestors1:
        return search2
      ancestors2.append(search2)
      search2 = search2.parent
      print(ancestors2)
  return None