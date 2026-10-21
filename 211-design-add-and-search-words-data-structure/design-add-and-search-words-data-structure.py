
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node

            char = word[i]

            if char == ".":
                for key in node:
                    if key != "#" and dfs(node[key], i + 1):
                        return True
                return False

            if char not in node:
                return False

            return dfs(node[char], i + 1)

        return dfs(self.root, 0)
