class PrefixTree:
    END_INDEX = 26

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord("a")
            curr_child = curr_node.child
            if not curr_child[index]:
                new_node = Node()
                curr_child[index] = new_node
            curr_node = curr_child[index]
        curr_node.child[self.END_INDEX] = Node()

    def search(self, word: str) -> bool:
        word += chr(ord("a")+26) 
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord("a")
            curr_child = curr_node.child
            if curr_child[index]:
                curr_node = curr_child[index]
            else:
                return False
        
        return True

class Node:
    def __init__(self):
        self.child = [None] * 27
