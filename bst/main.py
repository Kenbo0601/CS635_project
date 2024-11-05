from student_data import Student, Comparator
from binary_search_tree import BinarySearchTree
from tree_visitors import TreeVisitor


def main():
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


    # Unit test - Internal Iterator 
    iterator_test(bst)
    return 


# Unit test function for internal iterator 
def iterator_test(bst):

    # Use a lambda function to print each node's data
    print("In-order traversal output:")
    bst.for_each(lambda student: 
                 print(
                        student.get_first_name(), 
                        student.get_last_name(),
                        student.get_red_id(),
                        student.get_gpa()
                    )
                )

    # Use a lambda function to collect all nodes' values in a list
    node_values = []
    bst.for_each(lambda x: node_values.append(x))
    print("\nCollected node values:", node_values)

    return 


if __name__ == '__main__':
    main()


# Use visitor to count null nodes and calculate path lengths
'''visitor = TreeVisitor()
print("Number of null nodes:", visitor.count_null_nodes(bst.root))
longest_path = visitor.compute_paths(bst.root)
average_path_sum, node_count = visitor.average_path_length(bst.root)
average_path_length = average_path_sum / node_count if node_count else 0

print("Longest path length:", longest_path)
print("Average path length:", average_path_length)'''
