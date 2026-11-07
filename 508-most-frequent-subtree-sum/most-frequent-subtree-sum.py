# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        from collections import Counter

        freq = Counter()

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())
        return [s for s, count in freq.items() if count == max_freq]    