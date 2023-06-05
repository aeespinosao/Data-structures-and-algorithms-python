from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def add_node(self,value):
        self.nodes.add(value)
    
    def add_edge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path

customGraph = Graph()
customGraph.add_node("A")
customGraph.add_node("B")
customGraph.add_node("C")
customGraph.add_node("D")
customGraph.add_node("E")
customGraph.add_node("F")
customGraph.add_node("G")
customGraph.add_edge("A", "B", 2)
customGraph.add_edge("A", "C", 5)
customGraph.add_edge("B", "C", 6)
customGraph.add_edge("B", "D", 1)
customGraph.add_edge("B", "E", 3)
customGraph.add_edge("C", "F", 8)
customGraph.add_edge("D", "E", 4)
customGraph.add_edge("E", "G", 9)
customGraph.add_edge("F", "G", 7)

print(dijkstra(customGraph, "A"))