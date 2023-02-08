class Graph:
    def __init__(self,gDict=None):
        if gDict == None:
            self.gDict = {}
        self.gDict = gDict
    
    #function bfs(start,end):
    def bfs(self,start,end):
        queue = [start]
        visited = []
        parent = {start:None}
        while queue:
            #visiting node
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                #visit all chilren of node
                for child in self.gDict[node]:
                    if child not in visited:
                        queue.append(child)
                        if child not in parent.keys():
                            parent[child] = node
                        
        return self.reconstructPath(start,end,parent)
        
    #reconstrion function(start,end,parent):
    def reconstructPath(self,start,end,parentDict):
        path = []
        node = end
        #start loop from ptr=end and go until ptr!=None:
        while(node!=None):
            path.append(node)
            node = parentDict[node]
        return list(reversed(path))

myDict = {'a':['b','c'],'b':['a','d','g'],'c':['a','d','e'],'d':['b','c','f'],'e':['c','f'],'f':['d','e','g'],'g':['b','f']}
graph = Graph(myDict)
print(graph.gDict)
print('--------------------------------------')
print(graph.bfs('a','e'))
