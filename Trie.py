class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insertString(self,word):
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if node == None:
                newNode = TrieNode()
                current.children.update({letter:newNode})
            current = newNode
        current.endOfString = True
        print("Successfully inserted")
    
    def searchString(self,word):
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if node == None:
                return False
            current = node
        
        if current.endOfString is True:
            return True
        else:
            return False
            
def deleteString(root,word,index):
    ch = word[index]
    currentNo = root.children.get(ch)
    canThisStringBeDeleted = False
    if len(currentNode.children) > 1:
        deleteString(currentNode,word,index+1)
        return False
    
    if index == len(word)-1:
        if len(currentNode.children) >=1:
            currentNode.endOfString = False
        else:
            currentNode.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode,word,index+1)
        return False
        
    canThisStringBeDeleted = deleteString(currentNode,word,index+1)
    
    if canThisStringBeDeleted == True:
        currenNode.children.pop(ch)
        return True
    else:
        return False
    
    
trie = Trie()
print(trie.insertString("mango"))
print(trie.searchString("mangoe"))
