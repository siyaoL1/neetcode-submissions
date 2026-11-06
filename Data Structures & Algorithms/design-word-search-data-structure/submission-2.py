class Node:
    def __init__(self):
        self.children = {}  # 字符 -> Node
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True
        
    def search(self, word: str) -> bool:
        end_index = len(word)
        def helper(node, index):
            if index == end_index:
                return node.is_word


            c = word[index]
            if c == '.':
                return any(
                    helper(child, index + 1)
                    for child in node.children.values()
                    )
            elif c in node.children:
                return helper(node.children[c], index + 1)
            else:
                return False
        
        return helper(self.root, 0)
