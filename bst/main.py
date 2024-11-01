from student_data import Student, Comparator
from binary_search_tree import BinarySearchTree
from tree_visitors import TreeVisitor

# Create students
students = [
    Student("John", "Doe", 101, 3.5),
    Student("Jane", "Smith", 102, 3.7),
    Student("Alice", "Johnson", 103, 2.8)
]

# Create a tree using a specific comparator, e.g., by Red ID
bst = BinarySearchTree(Comparator.by_red_id)
for student in students:
    bst.add(student)

# Use internal iterator to print each student
bst.iterate(lambda student: print(student))

# Use visitor to count null nodes and calculate path lengths
visitor = TreeVisitor()
print("Number of null nodes:", visitor.count_null_nodes(bst.root))
longest_path = visitor.compute_paths(bst.root)
average_path_sum, node_count = visitor.average_path_length(bst.root)
average_path_length = average_path_sum / node_count if node_count else 0

print("Longest path length:", longest_path)
print("Average path length:", average_path_length)
