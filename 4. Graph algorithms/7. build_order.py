def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]


def projects_dependents(graph):
    dependents = [dep for dep_list in list(graph.values()) for dep in dep_list]
    return set(dependents)

def projects_independents(graph, dependents):
    all = set(graph.keys())
    return all.difference(dependents)
    
def findBuildOrder(projects, dependencies):
    graph = createGraph(projects, dependencies)
    solved = []
    while graph:
        dep = projects_dependents(graph)
        ind = projects_independents(graph, dep)
        
        if not ind and graph:
            raise ValueError('There is a cycle in the build order')
        
        for i in ind:
            solved.append(i)
            del graph[i]
    
    return solved

    
print(dep)
print(ind)