#Graph using adjecency list.
#create a graph class
class Graph:
    #add empty dictionary named adjecencyList in constructor.
    def __init__(self):
        self.adjecencyList = {}
    #add addVertex method
    def addVertex(self,vertex):
        #Check if vertex is already present or not. It not add it in adjecency list.
        if vertex not in self.adjecencyList.keys():
            self.adjecencyList[vertex] = []
    #add method to print this list.
    def printGraph(self):
        #use for iterator and .keys() method.
        for vertex in self.adjecencyList.keys():
            print(vertex,":",self.adjecencyList[vertex])
            
graph = Graph()
graph.addVertex('A')
graph.printGraph()
        
        
