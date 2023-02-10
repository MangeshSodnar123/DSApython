import heapq

class Edge:
    def __init__(self,weight,startVertex,endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex
        

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.minDistance = float('inf')
        self.neighbours = []
        self.predecessor = None
        
    def __lt__(self,otherNode):
        return self.minDistance < otherNode.minDistance
    
    def addEdge(self,otherNode,weight):
        edge = Edge(weight,self,otherNode)
        self.neighbours.append(edge)
        
class Dijkestra:
    def __init__(self):
        self.heap = []

    def calculate(self,startVertex):
        startVertex.minDistance = 0
        heapq.heappush(self.heap,startVertex)
        #run a while loop till heap not become empty.
        while self.heap:
            curVertex = heapq.heappop(self.heap)
            if curVertex.visited:
                continue
            #visit neighbours of curVertex:
            for edge in curVertex.neighbours:
                start = edge.startVertex
                end = edge.endVertex
                newDistance = start.minDistance + edge.weight
                if(newDistance < end.minDistance):
                    end.minDistance = newDistance
                    end.predecessor = start
                    heapq.heappush(self.heap,end)

            curVertex.visited = True
            
    def getShortestPath(self,endVertex):

        curVertex = endVertex

        print(f'the minimum distance is {endVertex.minDistance}')

        while (curVertex is not None):
            print(curVertex.name, end=" ")
            curVertex = curVertex.predecessor

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

nodeA.addEdge(nodeB,6)
nodeA.addEdge(nodeC,10)
nodeA.addEdge(nodeD,9)

nodeB.addEdge(nodeD,5)
nodeB.addEdge(nodeF,13)
nodeB.addEdge(nodeE,16)

nodeC.addEdge(nodeD,6)
nodeC.addEdge(nodeH,5)
nodeC.addEdge(nodeG,21)

nodeD.addEdge(nodeF,8)
nodeD.addEdge(nodeH,7)

nodeE.addEdge(nodeG,10)

nodeF.addEdge(nodeE,4)
nodeF.addEdge(nodeG,12)

nodeH.addEdge(nodeG,14)

dj = Dijkestra()
dj.calculate(nodeA)
dj.getShortestPath(nodeG)
