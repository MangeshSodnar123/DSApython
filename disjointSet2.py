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
        # get parents of both nodes
        #check if they belong to same parent
            #if yes then print msg saying they can't be joined.
        #else:
            #check rank of both parents:
            #Meke parent with bigger rank the parent of both families
            #make any parent a parent of both families if ranks are same
            #increase rank of final parent by 1
            
            
vertices = ['A','B','C','D','E','F']
ds = DisjointSet(vertices)
print(ds.find('A'))
