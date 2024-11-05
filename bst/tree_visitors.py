# tree_visitors.py
from abc import ABC, abstractmethod
from tree_nodes import TreeNodeInterface


class VisitorInterface(ABC):
    """Interface for implementing the Visitor Pattern on a binary search tree.
    
    Each visitor must implement the visit method, allowing it to traverse
    nodes in the tree to perform specific operations.
    """
    
    @abstractmethod
    def visit(self, node: TreeNodeInterface):
        """Defines a visit method to be applied to nodes in the tree."""
        pass


class NullNodeCounter(VisitorInterface):
    """Counts the number of NullNodes in a binary search tree.
    
    Attributes:
        null_count (int): The count of NullNodes encountered during traversal.
    """
    
    def __init__(self):
        self.null_count = 0
    
    def visit(self, node: TreeNodeInterface):
        """Visits each node in the tree and increments null_count for each NullNode.
        
        Args:
            node (TreeNodeInterface): The current node being visited.
        """
        if node.is_null():
            self.null_count += 1
        else:
            self.visit(node.left)
            self.visit(node.right)

    def get_null_count(self):
        """Returns the total count of NullNodes."""
        return self.null_count


class PathMetricsVisitor(VisitorInterface):
    """Calculates the longest path and average path length in a binary search tree.
    
    Attributes:
        longest_path (int): The longest path from the root to a leaf.
        path_length_sum (int): The cumulative length of all paths from the root.
        node_count (int): The total number of nodes encountered, excluding NullNodes.
    """
    
    def __init__(self):
        self.longest_path = 0
        self.path_length_sum = 0
        self.node_count = 0
    
    def visit(self, node: TreeNodeInterface, depth=0):
        """Visits each node to calculate path metrics, updating longest path
        and total path length.
        
        Args:
            node (TreeNodeInterface): The current node being visited.
            depth (int): Current depth level, starting at the root with 0.
        """
        if node.is_null():
            return depth
        else:
            left_depth = self.visit(node.left, depth + 1)
            right_depth = self.visit(node.right, depth + 1)
            current_depth = max(left_depth, right_depth)
            
            # Update path metrics
            self.longest_path = max(self.longest_path, current_depth)
            self.path_length_sum += depth
            self.node_count += 1

            # Return the current depth for recursive comparison
            return current_depth

    def get_longest_path(self):
        """Returns the length of the longest path in the tree."""
        return self.longest_path
    
    def get_average_path_length(self):
        """Returns the average path length in the tree."""
        return self.path_length_sum / self.node_count if self.node_count else 0
