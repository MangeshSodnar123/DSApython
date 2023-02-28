#you will need three hash tables
# graph,costs, parents
import math
INF = math.inf

#problem#1
# graph = {}
# graph['start'] = {}
# graph['start']['A'] = 6
# graph['start']['B'] = 2
# graph['A'] = {'final':1}
# graph['B'] = {'A':3,'final':5}
# graph['final'] = {}

# costs = {'A':6,'B':2,'final':INF}
# parents = {'start':None,'A':'start','B':'start','final':None}

# #problem#2
# graph = {}
# graph['start'] = {'a':5,'b':2}
# graph['a'] = {'c':4,'d':2}
# graph['b'] = {'a':8,'d':7}
# graph['c'] = {'d':6,'final':3}
# graph['d'] = {'final':1}
# graph['final'] = {}

# costs = {
#     'a':5,
#     'b':2,
#     'c':INF,
#     'd':INF,
#     'final':INF
# }

# parents = {
#     'start':None,
#     'a':'start',
#     'b':'start',
#     'c':None,
#     'd':None,
#     'final':None
# }

#problem#3
graph = {}


def findLowestNode(costDict,processed):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costDict:
        cost = costDict[node]
        if(cost)<lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

def tracePath(parents,final,costs):
    print(final,'->',end=' ')
    node = final
    par = parents[final]
    while par is not None:
        print(par,'->',end=" ")
        node = par
        par = parents[node]
    print('\nCost of travel is: ',costs[final])
    
#find the cheapest node.
def dijkestra(graph,costs,parents):
    processed = []
    node = findLowestNode(costs,processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            newCost = cost + neighbours[n]
            if newCost<costs[n]:
                costs[n] = newCost
                parents[n] = node
        processed.append(node)
        node = findLowestNode(costs,processed)
    tracePath(parents,'final',costs)
    
dijkestra(graph,costs,parents)
#update the costs of neighbours of this node.
#repeat until you done this for all nodes in the graph
#calculate the final path
