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
        #create a list for heap
        self.heap = []
    #calculate function(startVertex);
    def calculate(self,startVertex):
        #push start vertex to heap
        heapq.heappush(self.heap,startVertex)
        startVertex.minDistance = 0
        #run a while loop till heap not become empty.
        while self.heap:
            #curVertex = heap pop vertex
            curVertex = heapq.heappop(self.heap)
            #check if curVertex is visited or not:
            if curVertex.visited:
                #if yes 'continue'
                continue
            #visit neighbours of curVertex:
            for edge in curVertex.neighbours:
                #start = edge.startVertex
                start = edge.startVertex
                #end = edge.endVertex
                end = edge.endVertex
                newDistance = start.minDistance + edge.weight
                if(newDistance < end.minDistance):
                    end.minDistance = newDistance
                    end.predecessor = start
                    #heap.push(end)
                    heapq.heappush(self.heap,end)
            #curVertex.visited = true
            curVertex.visited = True
            
    #function to get shortest distance(endvertex):
    def getShortestPath(self,endVertex):
        #curVertex = endVertex
        curVertex = endVertex
        #print(minDistancd ov endVertex)
        print(f'the minimum distance from {self} to {endVertex} is {endVertex.minDistance}')
        #run a while loop to print path
        while curVertex:
            #curVertex = curVertex.predesessor to go back 
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
