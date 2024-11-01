from tree_nodes import TreeNode, NullNode

class BinarySearchTree:
    def __init__(self, comparator):
        self.root = NullNode()
        self.comparator = comparator

    def add(self, student):
        if self.root.is_null():
            self.root = TreeNode(student)
        else:
            self._add_recursive(self.root, student)

    def _add_recursive(self, node, student):
        if self.comparator(student, node.student) < 0:
            if node.left.is_null():
                node.left = TreeNode(student)
            else:
                self._add_recursive(node.left, student)
        else:
            if node.right.is_null():
                node.right = TreeNode(student)
            else:
                self._add_recursive(node.right, student)

    def iterate(self, func):
        self._iterate_recursive(self.root, func)

    def _iterate_recursive(self, node, func):
        if node.is_null():
            return
        self._iterate_recursive(node.left, func)
        func(node.student)
        self._iterate_recursive(node.right, func)
