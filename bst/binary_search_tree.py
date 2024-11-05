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


    # Internal Iterator Implementation 
    def for_each(self, action):
        self._for_each_recursive(self.root, action)

    # recursive helper function for for_each method 
    def _for_each_recursive(self, node, action):
        if node.is_null():
            return
        # inorder traversal 
        self._for_each_recursive(node.left, action)
        action(node.student)
        self._for_each_recursive(node.right, action)
