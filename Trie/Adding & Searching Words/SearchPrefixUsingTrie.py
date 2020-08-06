class Trie:

    def __init__(self):
        self.root = {'*':'*'}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = "*"
        
    def search(self, word: str) -> bool:
        curr_node = self.root
        
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        
        return '*' in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        
        for letter in prefix:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)