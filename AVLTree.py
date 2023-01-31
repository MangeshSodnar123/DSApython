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
        while not(len(customList)==0):
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

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

    
def getBalance(rootNode):
    if not rootNode:
        return
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

newAVL = AVLNode(30)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 35)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 50)
newAVL = insertNode(newAVL, 60)
newAVL = insertNode(newAVL, 70)
newAVL = insertNode(newAVL, 65)
preOrderTraversal(newAVL)

