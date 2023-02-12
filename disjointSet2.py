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
            
            
vertices = ['A','B','C','D','E','F','G']
ds = DisjointSet(vertices)
print(ds.find('A'))
ds.union('A','B')
ds.union('B','C')
ds.union('C','D')
ds.union('E','F')
ds.union('B','D')

print(ds.parent)
