"""
null_node_counter.py

Implements NullNodeCounter, a visitor class to count null nodes in a binary search tree.
This class is designed to work with the BinarySearchTree structure and utilizes the 
Visitor Pattern. It traverses the tree, counting all instances of NullNode.
"""

class NullNodeCounter:
    """
    NullNodeCounter is a visitor class that counts the number of null nodes in a binary search tree.

    Attributes:
    -----------
    null_count : int
        The number of null nodes encountered during the tree traversal.

    Methods:
    --------
    visit(node):
        Recursively visits each node in the tree to count the NullNode instances.
    """

    def __init__(self):
        self.null_count = 0

    def visit(self, node):
        """
        Recursively visits each node in the tree, counting NullNode instances.

        Parameters:
        -----------
        node : TreeNode or NullNode
            The current node being visited in the tree traversal.
        """
        if node.is_null():
            self.null_count += 1
        else:
            # Continue traversal on non-null nodes
            self.visit(node.left)
            self.visit(node.right)

    def get_null_count(self):
        """
        Returns the total count of null nodes after traversal.

        Returns:
        --------
        int
            The number of null nodes counted in the tree.
        """
        return self.null_count
