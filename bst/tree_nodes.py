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

    @abstractmethod
    def insert(self, student, strategy):
        pass

    @abstractmethod
    def for_each(self,action):
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

    def insert(self, student, strategy):
        if strategy.compare(student, self.student) < 0:
            self.left = self.left.insert(student, strategy)
        else:
            self.right = self.right.insert(student, strategy)
        return self

    def for_each(self, action):
        self.left.for_each(action)
        action(self.student)
        self.right.for_each(action)
    
    

# Null Object Class
class NullNode(TreeNodeInterface):

    def __init__(self, student=None):
        self.student = student

    def is_null(self):
        return True
    
    def __repr__(self):
        return "NullNode"

    def accept(self, visitor):
        visitor.visit(self)
    
    def insert(self, student, strategy):
        return TreeNode(student)
    
    def for_each(self, action):
        # Do nothing since this is a null node
        pass