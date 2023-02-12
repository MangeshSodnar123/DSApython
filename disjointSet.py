def getParent(graph,node):
    if graph[node]<0:
        return node
    else:
        getParent(graph,graph[node])

def union(graph,node1,node2):
    par1 = getParent(graph,node1)
    par2 = getParent(graph,node2)

    if par1 == par2:
        print('nodes Cannot be connected',node1,node2)
    else:
        if graph[par1] == graph[par2]:
            graph[par1] = graph[par1] + graph[par2]
            graph[par2] = par1
            
        else:
            if graph[par1] < graph[par2]:
                graph[par1] = graph[par1] + graph[par2]
                graph[par2] = par1
            else:
                graph[par2] = graph[par2] + graph[par1]
                graph[par1] = par2
