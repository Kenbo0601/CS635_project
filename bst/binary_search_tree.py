from tree_nodes import TreeNode, NullNode
from comparator import ComparatorStrategy

class BinarySearchTree:
    def __init__(self):
        self.root = NullNode()
    
    def set_strategy(self, strategy: ComparatorStrategy):
        self.strategy = strategy

    def insert(self, student):
        self.root = self.root.insert(student, self.strategy)

    # Internal Iterator Implementation 
    def for_each(self, action):
        self.root.for_each(action)

    def accept(self, visitor):
        return self.root.accept(visitor)
