from tree_nodes import TreeNode, NullNode
from comparator import ComparatorStrategy

class BinarySearchTree:
    def __init__(self):
        # Initialize the Binary Search Tree with a root node set to NullNode
        # This allows the tree to use the Null Object pattern for empty trees
        self.root = NullNode()
    
    def set_strategy(self, strategy: ComparatorStrategy):
        # Set a comparison strategy to be used for node insertion and other operations
        # Strategy pattern allows for flexible sorting/comparison of nodes (e.g., by different fields of 'student')
        self.strategy = strategy

    def insert(self, student):
        # Insert a new student node into the tree
        # Uses the current comparison strategy to find the correct location in the tree
        self.root = self.root.insert(student, self.strategy)

    # Internal Iterator Implementation
    def for_each(self, action):
        # Traverse the tree and apply a given action to each node
        # The action function is applied to each node in a specific traversal order
        self.root.for_each(action)

    def accept(self, visitor):
        # Accept a visitor object that performs an operation on the tree
        # Allows for implementing the Visitor pattern, useful for operations like traversals and aggregations
        return self.root.accept(visitor)
