from student import Student
from comparator import ComparatorStrategy, ByNameComparator, ByRedIdComarator, ByRoundedGPAComparator
from binary_search_tree import BinarySearchTree
from tree_visitors import VisitorInterface, NullNodeCounter, PathMetricsVisitor


def main():
    # Create students
    students = [
        Student("John", "Doe", 101, 3.5),
        Student("Jane", "Smith", 102, 3.7),
        Student("Alice", "Johnson", 103, 2.8)
    ]

    # Create a tree using a specific comparator
    redIdComparator = ByRedIdComarator()
    nameComparator = ByNameComparator()
    gpaComparator = ByRoundedGPAComparator()

    # Order tree by specific strategy 
    order_tree_by_redId(students, redIdComparator)
    order_tree_by_name(students, nameComparator) 
    order_tree_by_gpa(students, gpaComparator)
    return 


def order_tree_by_redId(students, strategy):
    print("\n\n --- Order Tree by RedId Strategy --- \n")
    bst = BinarySearchTree()
    bst.set_strategy(strategy)

    for student in students:
        bst.add(student)

    # Unit test - Internal Iterator 
    iterator_test(bst)

    # Use visitors to analyze the tree
    apply_visitors(bst)


def order_tree_by_name(students, strategy):
    print("\n\n --- Order Tree by Name Strategy --- \n")
    bst = BinarySearchTree()
    bst.set_strategy(strategy)
    
    for student in students:
        bst.add(student)

    # Unit test - Internal Iterator 
    iterator_test(bst)

    # Use visitors to analyze the tree
    apply_visitors(bst)


def order_tree_by_gpa(students, strategy):
    print("\n\n --- Order Tree by GPA Strategy --- \n")
    bst = BinarySearchTree()
    bst.set_strategy(strategy)
    
    for student in students:
        bst.add(student)

    # Unit test - Internal Iterator 
    iterator_test(bst)

    # Use visitors to analyze the tree
    apply_visitors(bst)



# Unit test function for internal iterator 
def iterator_test(bst):

    print("\n ### Iterator Test ### ")
    print(" --------------------- ")
    # Use a lambda function to print each node's data
    print("In-order traversal output:")
    bst.for_each(lambda student: print(student))

    # Use a lambda function to collect all nodes' values in a list
    print("\nCollect nodes in a list:")
    node_values = []
    bst.for_each(lambda student: node_values.append(student))
    print("Collected node values:", node_values)


def apply_visitors(bst):
    """
    Applies visitor objects to the BST to count null nodes, compute longest path, and calculate average path length.
    """
    print("\n ### Visitor Test ### ")
    print(" -------------------- ")
    # Use NullNodeCounter visitor
    null_node_counter: VisitorInterface = NullNodeCounter()
    bst.accept(null_node_counter)
    print("\nNumber of null nodes:", null_node_counter.get_null_count())

    # Use PathMetricsVisitor
    path_metrics_visitor: VisitorInterface = PathMetricsVisitor()
    bst.accept(path_metrics_visitor)
    print("Longest path length:", path_metrics_visitor.get_longest_path())
    print("Average path length:", path_metrics_visitor.get_average_path_length())


if __name__ == '__main__':
    main()
