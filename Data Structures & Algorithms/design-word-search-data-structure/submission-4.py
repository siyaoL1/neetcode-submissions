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
        def match(node: Node, index: int) -> bool:
            if index == len(word):
                return node.is_word

            char = word[index]
            if char == ".":
                return any(
                    match(child, index + 1)
                    for child in node.children.values()
                )

            child = node.children.get(char)
            return child is not None and match(child, index + 1)

        return match(self.root, 0)
