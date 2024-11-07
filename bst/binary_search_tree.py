from tree_nodes import TreeNode, NullNode, NodeFactory
from comparator import ComparatorStrategy

class BinarySearchTree:
    def __init__(self):
        self.factory = NodeFactory() 
        self.root = self.factory.create_null_node()
    
    def set_strategy(self, strategy: ComparatorStrategy):
        self.strategy = strategy

    def insert(self, student):
        self.root = self.factory.insert(self.root, student, self.strategy)

    # Internal Iterator Implementation 
    def for_each(self, action):
        self.factory.for_each_recursive(self.root, action)

    def accept(self, visitor):
        return self.root.accept(visitor)
