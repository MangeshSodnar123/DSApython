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
            return True
        return False
    #add method to print this list.
    def printGraph(self):
        #use for iterator and .keys() method.
        for vertex in self.adjecencyList.keys():
            print(vertex,":",self.adjecencyList[vertex])
            
    #method to add edge with parameters:vertex1,vertext2->bool
    def addEdge(self,vertex1,vertex2):
        #First check if both vertices are present in our dictionary or not. if not return false. else add edge and return true.
        if vertex1 in self.adjecencyList.keys() and vertex2 in self.adjecencyList.keys():
            self.adjecencyList[vertex1].append(vertex2)
            self.adjecencyList[vertex2].append(vertex1)
            return True
        return False
        
    #method to remove edge(vertex1,vertex2)->bool
    def removeEdge(self,vertex1,vertex2):
        #check if vertices are present in dict. if yes use .remove() method of the dict.
        if vertex1 in self.adjecencyList.keys() and vertex2 in self.adjecencyList.keys():
            try:
                self.adjecencyList[vertex1].remove(vertex2)
                self.adjecencyList[vertex2].remove(vertex1)
            except Exception:
                pass
            return True
        return False
        
graph = Graph()
graph.addVertex('A')
graph.addVertex('B')
graph.addEdge('A','B')
graph.printGraph()
print("---------------------")
graph.removeEdge('A','B')
graph.printGraph()
        
        
