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
    
    
trie = Trie()
print(trie.insertString("mango"))
print(trie.searchString("mangoe"))
