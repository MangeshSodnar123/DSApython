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

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


def deleteNode(rootNode,nodeValue):
############### my code ##################

    if not rootNode:
        return rooNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
        
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.righChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode.leftChild)
    return rootNode
    
def deleteAVL

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
print("-----------")
deleteNode(newAVL,25)
preOrderTraversal(newAVL)

