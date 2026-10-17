# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        positions = {value: i for i, value in enumerate(inorder)}
        post_index = len(postorder) - 1

        def build(left, right):
            nonlocal post_index

            if left > right:
                return None

            root_value = postorder[post_index]
            post_index -= 1

            root = TreeNode(root_value)
            mid = positions[root_value]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
    