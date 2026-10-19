
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in word_set and new_word not in visited:
                            if new_word not in level_visited:
                                level_visited.add(new_word)
                                queue.append(new_word)

                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

            visited.update(level_visited)

        if not found:
            return []

        result = []
        path = [endWord]

        def build_path(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                build_path(parent)
                path.pop()

        build_path(endWord)
        return result
