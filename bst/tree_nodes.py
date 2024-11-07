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

    def __init__(self, student=None):
        self.student = student

    def is_null(self):
        return True
    
    def __repr__(self):
        return "NullNode"

    def accept(self, visitor):
        visitor.visit(self)


# Node factory class - handles operations for tree 
class NodeFactory:
    def create_node(self, student):
        return TreeNode(student)
    
    def create_null_node(self):
        return NullNode()
    
    def insert(self, node, student, strategy):
        if node.is_null():
            return self.create_node(student)
        else:
            return self._insert(node, student, strategy) 

    def _insert(self, node, student, strategy):
        if strategy.compare(student, node.student) < 0:
            if node.left.is_null():
                node.left = self.create_node(student)
            else:
                self._insert(node.left, student, strategy)
        else:
            if node.right.is_null():
                node.right = self.create_node(student)
            else:
                self._insert(node.right, student, strategy)
        return node
    
    def for_each_recursive(self, node, action):
        if node.is_null():
            return

        # inorder traversal 
        self.for_each_recursive(node.left, action)
        action(node.student)
        self.for_each_recursive(node.right, action)
        return 

        
    
