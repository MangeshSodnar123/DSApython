class Graph:
    def __init__(self,gDict=None):
        if gDict==None:
            self.gDict = {}
        self.gDict = gDict
    
    def addEdge(self,vertex,edge):
        self.gDict[vertex].append(edge)
    
    def bft(self,vertex):
        #declare list for visited and initiate it with vertex
        visited = [vertex]
        #declare list for queue and initiate it with vertex.
        queue = [vertex]
        #while(queue):
        while(queue):
            #dequeue the element and print it
            dVertex = queue.pop(0)
            print(dVertex)
            #check if all element from edge list of dVertex is visited.
            for adjVertex in self.gDict[dVertex]:
                if adjVertex not in visited:
                    #if not then enqueue it in queue and
                    queue.append(adjVertex)
                    # add it to visited list.
                    visited.append(adjVertex)
                
myDict = {'a':['b','c'],'b':['a','d','e'],'c':['a','e'],'d':['b','e','f'],'e':['b','c','d','f'],'f':['d','e']}

graph = Graph(myDict)
graph.bft('a')
