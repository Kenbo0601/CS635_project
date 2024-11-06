from abc import ABC, abstractmethod

'''
Applying Null Object Pattern on Node class 
'''

# TreeNode interface 
class TreeNodeInterface(ABC):
    @abstractmethod
    def is_null(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass 

# Real Object Class 
class TreeNode(TreeNodeInterface):
    def __init__(self, student=None, left=None, right=None):
        self.student = student
        self.left = NullNode()
        self.right = NullNode()

    def is_null(self):
        return False

    def __repr__(self):
        return f"TreeNode({self.student})"

    def accept(self, visitor):
        visitor.visit(self)
    

# Null Object Class
class NullNode(TreeNodeInterface):
    def is_null(self):
        return True

    def __repr__(self):
        return "NullNode"

    def accept(self, visitor):
        visitor.visit(self)