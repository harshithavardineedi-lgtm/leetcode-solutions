from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            maximum = float('-inf')

            for _ in range(size):
                node = queue.popleft()
                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(maximum)

        return result    