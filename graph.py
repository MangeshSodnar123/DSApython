#graph
#create graph class with the help of python dictionary.
class Graph:
    def __init__(self,gDict=None):
        if gDict is None:
            self.gDict = {}
        else:
            self.gDict = gDict
    
    #create addEdge method in it.
    def addEdge(self,vertex,edge):
        self.gDict[vertex].append(edge)
        
#initialize the graph class with customDict
myDict = {'a':['b','c'],'b':['a','e','d'],'c':['a','e'],'d':['b','e','f'],'e':['b','d','f'],'f':['d','e']}
graph = Graph(myDict)
#print the dictionary.
print(graph.gDict)
print("-------------------------------------------")
graph.addEdge('a','z')
print(graph.gDict)
