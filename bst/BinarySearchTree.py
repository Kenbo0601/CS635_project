from abc import ABC, abstractmethod
from math import isclose


class Student:
    def __init__(self, first_name, last_name, red_id, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.red_id = red_id
        self.gpa = gpa

    def __str__(self):
        return f"{self.first_name} {self.last_name}, RedID: {self.red_id}, GPA: {self.gpa}"


# Strategy Pattern
class SortStrategy(ABC):
    @abstractmethod
    def compare(self, student1, student2):
        pass


class SortByRedID(SortStrategy):
    def compare(self, student1, student2):
        return student1.red_id - student2.red_id


class SortByName(SortStrategy):
    def compare(self, student1, student2):
        if student1.last_name != student2.last_name:
            return (student1.last_name > student2.last_name) - (student1.last_name < student2.last_name)
        return (student1.first_name > student2.first_name) - (student1.first_name < student2.first_name)



class SortByRoundedGPA(SortStrategy):
    def compare(self, student1, student2):
        rounded_gpa1 = round(student1.gpa)
        rounded_gpa2 = round(student2.gpa)
        if rounded_gpa1 == rounded_gpa2:
            return student1.red_id - student2.red_id
        return rounded_gpa1 - rounded_gpa2


# Null Object Pattern
class NullNode:
    def __init__(self):
        pass

    def insert(self, student, bst):
        return BSTNode(student, NullNode(), NullNode())

    def accept(self, visitor, depth = 0):
        visitor.visit_null(self)

    def __str__(self):
        return "NullNode"


# Binary Search Tree Node
class BSTNode:
    def __init__(self, student, left=None, right=None):
        self.student = student
        self.left = left or NullNode()
        self.right = right or NullNode()

    def insert(self, student, bst):
        if bst.strategy.compare(student, self.student) < 0:
            self.left = self.left.insert(student, bst)
        else:
            self.right = self.right.insert(student, bst)
        return self

    def accept(self, visitor, depth = 0):
        visitor.visit_node(self, depth)
        self.left.accept(visitor, depth + 1)
        self.right.accept(visitor, depth + 1)


# Binary Search Tree
class BinarySearchTree:
    def __init__(self, strategy):
        self.root = NullNode()  # Root starts as a NullNode
        self.strategy = strategy  # Sorting strategy determines insertion order

    def insert(self, student):
        self.root = self.root.insert(student, self)

    def traverse(self, action):
        def _traverse(node):
            if isinstance(node, NullNode):
                return
            _traverse(node.left)
            action(node.student)
            _traverse(node.right)

        _traverse(self.root)

    def accept(self, visitor):
        self.root.accept(visitor)



# Visitor Pattern
class Visitor(ABC):
    @abstractmethod
    def visit_node(self, node):
        pass

    @abstractmethod
    def visit_null(self, null_node):
        pass


class NullNodeCounter(Visitor):
    def __init__(self):
        self.count = 0

    def visit_node(self, node, depth):
        pass

    def visit_null(self, null_node):
        self.count += 1


class PathLengthVisitor(Visitor):
    def __init__(self):
        self.longest_path = 0
        self.total_path_length = 0
        self.total_nodes = 0

    def visit_node(self, node, depth):
        self.total_nodes += 1
        self.total_path_length += depth
        depth += 1
        self.longest_path = max(self.longest_path, depth)

    def visit_null(self, null_node):
        pass


# Main Example
if __name__ == "__main__":
    students = [
        Student("Kenichi", "Sakamoto", 2924, 4.0),
        Student("Dan", "Houston", 7516, 4.0),
        Student("Hyunhee", "Kwak", 9458, 3.9),
    ]

    # Create BST with byRedID strategy
    bst_ID = BinarySearchTree(SortByRedID())
    for student in students:
        bst_ID.insert(student)

    # Internal Iterator
    print("Traversing ID_BST:")
    bst_ID.traverse(lambda student: print(student))

    # Visitor Example
    null_counter = NullNodeCounter()
    bst_ID.accept(null_counter)
    print(f"Number of null nodes: {null_counter.count}")

    path_visitor = PathLengthVisitor()
    bst_ID.accept(path_visitor)
    print(f"Longest path: {path_visitor.longest_path}")
    print(f"Average path length: {path_visitor.total_path_length / path_visitor.total_nodes if path_visitor.total_nodes > 0 else 0}")

    # Create BST with byName strategy
    bst_name = BinarySearchTree(SortByName())
    for student in students:
        bst_name.insert(student)

    # Internal Iterator
    print("Traversing Name_BST:")
    bst_name.traverse(lambda student: print(student))

    # Visitor Example
    null_counter = NullNodeCounter()
    bst_name.accept(null_counter)
    print(f"Number of null nodes: {null_counter.count}")

    path_visitor = PathLengthVisitor()
    bst_name.accept(path_visitor)
    print(f"Longest path: {path_visitor.longest_path}")
    print(f"Average path length: {path_visitor.total_path_length / path_visitor.total_nodes if path_visitor.total_nodes > 0 else 0}")

    # Create BST with byGPA strategy
    bst_gpa = BinarySearchTree(SortByRoundedGPA())
    for student in students:
        bst_gpa.insert(student)

    # Internal Iterator
    print("Traversing GPA_BST:")
    bst_gpa.traverse(lambda student: print(student))

    # Visitor Example
    null_counter = NullNodeCounter()
    bst_gpa.accept(null_counter)
    print(f"Number of null nodes: {null_counter.count}")

    path_visitor = PathLengthVisitor()
    bst_gpa.accept(path_visitor)
    print(f"Longest path: {path_visitor.longest_path}")
    print(f"Average path length: {path_visitor.total_path_length / path_visitor.total_nodes if path_visitor.total_nodes > 0 else 0}")
