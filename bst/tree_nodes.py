from abc import ABC, abstractmethod

# TreeNode interface 
class TreeNodeInterface(ABC):
    @abstractmethod
    def is_null(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class TreeNode(TreeNodeInterface):
    def __init__(self, student=None, left=None, right=None):
        self.student = student
        self.left = left if left else NullNode()
        self.right = right if right else NullNode()

    def is_null(self):
        return False

    def __repr__(self):
        return f"TreeNode({self.student})"


class NullNode(TreeNodeInterface):
    def is_null(self):
        return True

    def __repr__(self):
        return "NullNode"
