#create method
#declare a class named DisjointSet
class DisjointSet:
    #take(vertises list as parameter)
    def __init__(self,vertices):
    #create rank dictionary and put defalult values 0 for all keys(vertices)
        self.vertices = vertices
        self.rank = dict.fromkeys(self.vertices,0)
    #create parent dictionary and put vertex as a parent of itself
        self.parent = {}
        for vertex in vertices:
            self.parent[vertex] = vertex
    
    #find method(node)
    def find(self,vertex):
        #check if parent of node is node itself:
        if self.parent[vertex] == vertex:
            #if yes return node
            return vertex
        else:
            #return : call find function recursively till above condition becomes true
            return self.find(self.parent[vertex])
            
    #union method(node1,node2)
    def union(self,vertex1,vertex2):
        # get parents of both nodes
        par1 = self.find(vertex1)
        par2 = self.find(vertex2)
        #check if they belong to same parent
        if par1 == par2:
            #if yes then print msg saying they can't be joined.
            print(f'{vertex1} and {vertex2} cannot be joined as both have {par1} as a common parent')
        else:
            #check rank of both parents:
            if self.rank[par1] > self.rank[par2]:
                self.parent[par2] = par1
                self.rank[par1] += 1
            #Meke parent with bigger rank the parent of both families
            elif self.rank[par2] > self.rank[par1]:
            #make any parent a parent of both families if ranks are same
                self.parent[par1] = par2
                self.rank[par2] += 1
            else:
                self.parent[par2] = par1
                self.rank[par1] += 1
            #increase rank of final parent by 1
            
            
            
class Graph:
    #declare list for nodes,edges(graph)
    def __init__(self,vertices):
        self.V = vertices
        self.nodes = []
        self.graph = []
        self.MST = []
    #add addNode method(node)
    def addNode(self,node):
        #append to the nodes list
        self.nodes.append(node)
    
    #add addEdge method(start,destination,weight):
    def addEdge(self,start,destination,weight):
        #append to edges list
        self.graph.append([start,destination,weight])
    #add Print method
    def printGraph(self,graph):
        #run a loop for all the edges in the graph and print them all
        for start,destination,weight in graph:
            print(f'{start} -> {destination} : {weight}')
            
#declare a Kruskal function
    def kruskal(self):
        index = 0
        i = 0
        ds = DisjointSet(self.nodes)
    #take a list of edges as a input
    #sort that list based on the weight of edges ascending
        self.graph = sorted(self.graph,key=lambda item:item[2])
    #declare empty list to store the end result edges
    #run a loop to visit all edges from the sorted list.
        while index<self.V-1:
            #check if parent of the start and end are not same:
            s,d,w = self.graph[i]
            i += 1
            par1 = ds.find(s)
            par2 = ds.find(d)
            
            if par1 != par2:
                self.MST.append([s,d,w])
                ds.union(par1,par2)
                index += 1
                #if not same then append this pair in answer list
                #make union of the parents in the original list.
        #print the answer list
        self.printGraph(self.MST)
        
g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskal()
