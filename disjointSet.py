def getParent(graph,node):
    if graph[node]<0:
        return node
    else:
        parent = getParent(graph,graph[node])
        graph[node] = parent
        return parent

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
                
n = 7
graph = {}
for i in range(n):
    graph[i] = -1
    
ipt = [[0,1],[1,2],[2,3],[4,5]]

for u,v in ipt:
    graph[u] = v

print(graph)
print(getParent(graph,0))
print('______________')
union(graph,1,4)
print(graph)
