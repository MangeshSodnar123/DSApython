##Floyd Warshall

INF = 9999
#Printing the solution
def printSolution(noOfVertices,graph):
    n = noOfVertices
    for i in range(n):
        for j in range(n):
            if(graph[i][j]==INF):
                print('INF', end=' ')
            else:
                print(graph[i][j],end='  ')
        print()

#actual algorithm 
def floydWarshal(noOfVertices,graph):
    matrix = graph
    n = noOfVertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    printSolution(n,matrix)
    
    
G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floydWarshal(4, G)
