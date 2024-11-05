"""
path_metrics_visitor.py

Implements PathMetricsVisitor, a visitor class that computes the longest path
and the average path length of nodes in a binary search tree. This class uses
the Visitor Pattern to traverse the tree and calculate path metrics.
"""

class PathMetricsVisitor:
    """
    PathMetricsVisitor is a visitor class that calculates path-related metrics in a binary search tree,
    including the longest path from the root and the average path length of all nodes.

    Attributes:
    -----------
    longest_path : int
        Stores the length of the longest path encountered during traversal.

    total_path_length : int
        Cumulative sum of path lengths from the root to each node, used to compute the average path.

    node_count : int
        Counts the number of non-null nodes in the tree.

    Methods:
    --------
    visit(node, depth=0):
        Recursively visits each node to calculate path metrics.

    get_longest_path():
        Returns the longest path length found in the tree.

    get_average_path_length():
        Computes the average path length based on total path length and node count.
    """

    def __init__(self):
        self.longest_path = 0
        self.total_path_length = 0
        self.node_count = 0

    def visit(self, node, depth=0):
        """
        Recursively visits each node in the tree to compute path metrics.

        Parameters:
        -----------
        node : TreeNode or NullNode
            The current node being visited in the tree traversal.

        depth : int, default=0
            The current depth from the root to the node.
        """
        if node.is_null():
            return

        # Update path metrics
        self.longest_path = max(self.longest_path, depth)
        self.total_path_length += depth
        self.node_count += 1

        # Recursively visit left and right children
        self.visit(node.left, depth + 1)
        self.visit(node.right, depth + 1)

    def get_longest_path(self):
        """
        Returns the longest path length from the root to a leaf node.

        Returns:
        --------
        int
            The length of the longest path in the tree.
        """
        return self.longest_path

    def get_average_path_length(self):
        """
        Computes the average path length from the root to all nodes.

        Returns:
        --------
        float
            The average path length from the root to each node, or 0 if there are no nodes.
        """
        return self.total_path_length / self.node_count if self.node_count > 0 else 0
