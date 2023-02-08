class Graph:
    def __init__(self,gDict=None):
        if gDict == None:
            self.gDict = {}
        self.gDict = gDict
    
    #function bfs(start,end):
    def bfs(self,start,end):
        #queue = [start]
        queue = [start]
        #visited = []
        visited = []
        #parent = { start:None}
        parent = {start:None}
        #while queue is not empty:
        while queue:
            #node = dequeue the queue
            node = queue.pop(0)
            #check if node in visited:
            if node not in visited:
                #if not add it in visited else contineu.
                visited.append(node)
                #visit all chilren of node
                for child in self.gDict[node]:
                    #check if child present in visited
                    if child not in visited:
                        #if not add it in the queue
                        queue.append(child)
                        #check if child is present in parent dict:
                        if child not in parent.keys():
                            #if not parent[child] = node
                            parent[child] = node
                            
        # return reconstructedPath(start,end,dict)
        return self.reconstructPath(start,end,parent)
        
    #reconstrion function(start,end,parent):
    def reconstructPath(self,start,end,parentDict):
        #path = []
        path = []
        node = end
        #start loop from ptr=end and go until ptr!=None:
        while(node!=None):
            #path.append[ptr]
            path.append(node)
            #ptr = parent[ptr]
            node = parentDict[node]
        #return path
        path = path.reverse()
        return path

myDict = {'a':['b','c'],'b':['a','d','g'],'c':['a','d','e'],'d':['b','c','f'],'e':['c','f'],'f':['d','e','g'],'g':['b','f']}
graph = Graph(myDict)
print(graph.gDict)
print('--------------------------------------')
print(graph.bfs('a','f'))
