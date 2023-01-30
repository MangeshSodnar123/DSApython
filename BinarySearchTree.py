class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
            
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
        
def searchInBST(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        return "success"
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            return "success"
        else:
            searchInBST(rootNode.leftChild,nodeValue)
    else:
        if nodeValue == rootNode.rightChild.data:
            return "success"
        else:
            searchInBST(rootNode.rightChild,nodeValue)
    #return "Not found."

def inOrderPredecessor(rootNode):
    current = rootNode.leftChild
    while(current.rightChild is not None):
        current = current.rightChild
    return current
    
def deleteNode(rootNode,nodeValue):
    #base condition of recursion
    #if rootNode don's exist
    if (rootNode == None):
        return None
    #if rootNode is leafNode
    if (rootNode.leftChild == None and rootNode.rightChild == None):
        rootNode = None
        return None
    #search for the node
    if (nodeValue < rootNode.data):
        deleteNode(rootNode.leftChild,nodeValue)
    elif(nodeValue > rootNode.data):
        deleteNode(rootNode.rightChild,nodeValue)
    #delete node when found
    else:
        ipre = inOrderPredecessor(rootNode)
        rootNode.data = ipre.data
        rootNode.leftChild = deleteNode(rootNode.leftChild,ipre.data)
    
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "successfully delete."
        
bst = BSTNode(None)
insertNode(bst,90)
insertNode(bst,100)
insertNode(bst,80)
insertNode(bst,70)
insertNode(bst,60)
insertNode(bst,50)
inOrderTraversal(bst)
print("----------------")
deleteNode(bst,60)
inOrderTraversal(bst)
