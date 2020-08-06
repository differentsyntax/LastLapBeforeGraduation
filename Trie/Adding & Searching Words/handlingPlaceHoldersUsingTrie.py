class WordDictionary:

    def __init__(self):
        self.root = {'*':'*'}

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = "*"
        
    def search(self, word: str) -> bool:
        
        curr_node = self.root
        
        return self.dot(word, curr_node)
    
    def dot(self, word, curr_node):
        
        if len(word) == 0:
            return "*" in curr_node
            
        if word[0] == '.':
            for key in curr_node:
                if key != "*":
                    if self.dot(word[1:], curr_node[key]):
                        return True
            return False
        
        if word[0] in curr_node:
            curr_node = curr_node[word[0]]
            return self.dot(word[1:], curr_node)
        
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)