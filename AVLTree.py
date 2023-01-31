class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customList = []
        customList.append(rootNode)
        while not(len(customList == 0)):
            root = customList.pop(0)
            print(root.data)
            if root.leftChild is not None:
                customList.append(root.leftChild)
            if root.rightChild is not None:
                customList.append(root.rightChild)
        
def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print("success.")
        return
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("success.")
            return
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("success.")
            return
        else:
            searchNode(rootNode.rightChild,nodeValue)
    return 

#Insertion in avl tree
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height
    
def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    
    return newRoot
    
def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))

    return newRoot
    


avl = AVLNode(50)
