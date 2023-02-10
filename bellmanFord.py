
class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.node = []
    
    def addNode(self,node):
        self.node.append(node)
    
    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])
    
    def bellmanFord(self,src):
        dist = {x:float('Inf') for x in self.node}
        dist[src] = 0
        '''
        for i in range(self.v-1):
            for s,d,w in self.graph:
                if dist[s] != float('Inf') and (dist[s] + d < dist[d]):
                    dist[d] = dist[s] + d
        '''
        for _ in range(self.v-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        for i in range(self.v):
            for s,d,w in self.graph:
                if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                    print('Graph contains negative cycle.')
                    return
        self.printDist(dist)
            
    def printDist(self,dist):
        print('Distances are as follows: ')
        for key,value in dist.items():
            print(key,' : ',value)
        
        
g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")

