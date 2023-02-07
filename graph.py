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
                
    def dft(self,vertex):
        #declare list for visited = [vertex]
        visited = [vertex]
        # declare list for stack = [vertex]
        stack = [vertex]
        #run loop till stack becomes empty
        while stack:
            #pop last element from stack and print it
            popVertex = stack.pop()
            print(popVertex)
            #run a loop through all adjecent verteces of the vertex
            for adjVertex in self.gDict[popVertex]:
                #check if adject vertex present in visited list
                if adjVertex not in visited:
                    #if not then add it to visited list
                    visited.append(adjVertex)
                    #add it to the queue
                    stack.append(adjVertex)
    
myDict = {'a':['b','c'],'b':['a','d','e'],'c':['a','e'],'d':['b','e','f'],'e':['b','c','d','f'],'f':['d','e']}

graph = Graph(myDict)
graph.dft('a')
