###Binary tree using python list###

class BinaryTree:
    def __init__(self,size):
        self.list = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insert(self,value):
        if (self.lastUsedIndex + 1) == self.maxSize:
            return "The Binary tree is full."
        else:
            self.list[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
        
    def search(self,value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return "Success"
        return "Not found"
        
    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.list[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)
        
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.list[index])
        self.inOrderTraversal(index * 2 + 1)
        
    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.list[index])
        
    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.list[i])
        
    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "The binary tree is empty."
        for i in range(1,self.lastUsedIndex + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The node has been successfully deleted."
        
bt = BinaryTree(8)
bt.insert("Drinks")
bt.insert("Hot")
bt.insert("Cold")
bt.insert("Tea")
bt.insert("Coffee")
#print(bt.search("Tea"))
bt.levelOrderTraversal(1)
print("-----------------")
bt.deleteNode("Cold")
bt.levelOrderTraversal(1)
