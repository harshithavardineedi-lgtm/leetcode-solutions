
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self._leftmost_inorder(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
