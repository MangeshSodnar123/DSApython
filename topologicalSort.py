from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
        
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self,v,visited,stack):
        #first append v in the visited
        visited.append(v)
        #then visit all dependent nodes of v
        for k in self.graph[v]:
            #check if these nodes are present in the visited
            if k not in visited:
                #if not call topologicalSortUtil() recursiverly
                self.topologicalSortUtil(k,visited,stack)
                
        #push v to the stack
        stack.insert(0,v)
    
    def topologicalSort(self):
        #create list for visited
        visited = []
        #create stack
        stack = []
        #run a loop to visit all keys of the graph
        for i in list(self.graph):
            #check if that key is present  in the visited or not
                #if not call topologicalSortUtil() function
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
            
        #print the stack 
        print(stack)
        

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()
