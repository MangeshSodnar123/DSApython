class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
    def __str__(self):
        return str(self.value)

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
class Queue:
    def __init__(self):
        self.ll = LL()
        
    def __str__(self):
        values = [str(x) for x in self.ll]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.ll.head == None:
            return True
        else:
            return False
    
    def enqueue(self,value):
        node = Node(value)
        if self.isEmpty():
            self.ll.head = node
            self.ll.tail = node
        else:
            self.ll.tail.next = node
            self.ll.tail = node
    
    def dequeue(self):
        if self.isEmpty():
            return 
        else:
            val = self.ll.head.value
            self.ll.head = self.ll.head.next
            return val
'''q = Queue()
print(q.isEmpty())
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q)
print(q.isEmpty())'''

########################################################
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def __str__(self):
        return str(self.data)
    
newBt = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newBt.leftChild = hot
newBt.rightChild = cold
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee

def preOrderTraversal(treeNode):
    if not treeNode:
        return
    print(treeNode.data)
    preOrderTraversal(treeNode.leftChild)
    preOrderTraversal(treeNode.rightChild)

def inOrderTraversal(treeNode):
    if not treeNode:
        return
    inOrderTraversal(treeNode.leftChild)
    print(treeNode.data)
    inOrderTraversal(treeNode.rightChild)

def postOrderTraversal(treeNode):
    if not treeNode:
        return
    postOrderTraversal(treeNode.leftChild)
    postOrderTraversal(treeNode.rightChild)
    print(treeNode.data)
'''    
def levelOrderTraversal(rootNode):
    que = []
    que.append(rootNode)
    while que is not None:
        root = que.pop(0)
        print(root.data)
        if root.leftChild is not None:
            que.append(root.leftChild)
        if root.rightChild is not None:
            que.append(root.rightChild)
'''
def levelOrderTraversal(rootNode):
    que = Queue()
    que.enqueue(rootNode)
    while not(que.isEmpty()):
        root = que.dequeue()
        print(root.data)
        if root.leftChild is not None:
            que.enqueue(root.leftChild)
        if root.rightChild is not None:
            que.enqueue(root.rightChild)
   
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        que = Queue()
        que.enqueue(rootNode)
        while not(que.isEmpty()):
            root = que.dequeue()
            if (root.leftChild is not None):
                que.enqueue(root.leftChild)
            if (root.rightChild is not None):
                que.enqueue(root.rightChild)
        deepestNode = root
        return deepestNode

def deleteDeepestNode(rootNode,nodeVal):
    if not rootNode:
        return
    else:
        que = Queue()
        que.enqueue(rootNode)
        while not(que.isEmpty()):
            root = que.dequeue()
            if root == nodeVal:
                root = None
                return
            if (root.leftChild):
                if (root.leftChild==nodeVal):
                    root.leftChild = None
                    return
                else:
                    que.enqueue(root.leftChild)
            if (root.rightChild):
                if (root.rightChild==nodeVal):
                    root.rightChild = None
                    return
                else:
                    que.enqueue(root.rightChild)
        
def deleteNode(rootNode,nodeVal):
    if not rootNode:
        return
    else:
        que = Queue()
        que.enqueue(rootNode)
        deepestNode = getDeepestNode(rootNode)
        deleteDeepestNode(rootNode,deepestNode)
        while not(que.isEmpty()):
            root = que.dequeue()
            if root.data is nodeVal:
                root.data = deepestNode.data
            if (root.leftChild):
                if (root.leftChild.data==nodeVal):
                    root.leftChild.data = deepestNode.data
                    return
                else:
                    que.enqueue(root.leftChild)
            if (root.rightChild):
                if (root.rightChild.data==nodeVal):
                    root.rightChild.data = deepestNode.data
                    return
                else:
                    que.enqueue(root.rightChild)

levelOrderTraversal(newBt)
print("-------------------")
deleteNode(newBt,"Drinks")
'''dep = getDeepestNode(newBt)
print(dep)'''
print("-------------------")
levelOrderTraversal(newBt)
