
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        path = False
        while queue:
            deVertex = queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)
        return path
 
