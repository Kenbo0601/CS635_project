from abc import ABC, abstractmethod

'''
Applying Null Object Pattern on Node class
This pattern provides a NullNode class to represent empty nodes in the tree,
allowing the BinarySearchTree to handle null values more gracefully.
'''

# TreeNode interface
class TreeNodeInterface(ABC):
    @abstractmethod
    def is_null(self):
        # Determines if the node is a null node
        pass

    @abstractmethod
    def __repr__(self):
        # Provides a string representation of the node
        pass

    @abstractmethod
    def accept(self, visitor):
        # Accepts a visitor object for traversal or operation purposes
        pass 

    @abstractmethod
    def insert(self, student, strategy):
        # Inserts a student into the correct position based on the strategy
        pass

    @abstractmethod
    def for_each(self, action):
        # Applies an action to each node, following a traversal pattern
        pass


# Real Object Class
class TreeNode(TreeNodeInterface):
    def __init__(self, student=None, left=None, right=None):
        # Initialize a TreeNode with a student object and default left and right nodes as NullNodes
        self.student = student
        self.left = NullNode()
        self.right = NullNode()

    def is_null(self):
        # A TreeNode is never null, so this returns False
        return False
    
    def __repr__(self):
        # Provides a readable representation of the TreeNode, showing the student data
        return f"TreeNode({self.student})"

    def accept(self, visitor):
        # Accepts a visitor object and applies its visit method to this node
        visitor.visit(self)

    def insert(self, student, strategy):
        # Insert a new student node based on the given strategy:
        # - If the strategy comparison returns a negative value, insert into the left subtree
        # - Otherwise, insert into the right subtree
        if strategy.compare(student, self.student) < 0:
            self.left = self.left.insert(student, strategy)
        else:
            self.right = self.right.insert(student, strategy)
        return self

    def for_each(self, action):
        # Traverses the tree in-order and applies the action to each student:
        # - First traverses the left subtree, applies action to the current node, and then the right subtree
        self.left.for_each(action)
        action(self.student)
        self.right.for_each(action)


# Null Object Class
class NullNode(TreeNodeInterface):
    def __init__(self, student=None):
        # Initialize a NullNode, which holds no student data by definition
        self.student = student

    def is_null(self):
        # A NullNode is always considered null, so this returns True
        return True
    
    def __repr__(self):
        # Provides a representation of the NullNode, indicating it represents a null value
        return "NullNode"

    def accept(self, visitor):
        # Accepts a visitor and applies its visit method to this node
        visitor.visit(self)
    
    def insert(self, student, strategy):
        # When inserting into a NullNode, create a new TreeNode with the student data,
        # effectively replacing the NullNode in the tree
        return TreeNode(student)
    
    def for_each(self, action):
        # NullNode does nothing for for_each, as it represents an empty space in the tree
        pass
