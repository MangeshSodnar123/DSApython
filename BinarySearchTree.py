class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
            
def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
        

        
bst = BSTNode(100)
insertNode(bst,90)
insertNode(bst,80)
insertNode(bst,70)
insertNode(bst,60)
insertNode(bst,50)
inOrderTraversal(bst)
