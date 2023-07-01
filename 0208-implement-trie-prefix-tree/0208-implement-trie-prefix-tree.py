class Trie:


    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        
        for char in word:
            if char in current.keys():
                pass
            else:
                current[char] = {}
            current = current[char]

            
        if "end" not in current.keys():
            current["end"] = {}


    def search(self, word: str) -> bool:

        current = self.root
        for char in word:
            if char not in current.keys():
                return False

            current = current[char]

        if "end" in current:
            return True

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.keys():
                return False
            current = current[char]

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

