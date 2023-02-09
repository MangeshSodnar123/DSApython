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
        self.predesessor = None
        
    def __lt__(self,otherNode):
        return self.minDistance < otherNode.minDistance
    
    def addEdge(self,otherNode,weight):
        edge = Edge(weight,self,otherNode)
        self.neighbours.append(edge)
        
