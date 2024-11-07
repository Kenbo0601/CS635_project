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

    # Create a tree using a specific comparator, e.g., by Red ID
    redIdComparator = ByRedIdComarator()
    nameComparator = ByNameComparator()
    gpaComparator = ByRoundedGPAComparator()

    bst = BinarySearchTree()
    #bst.set_strategy(redIdComparator)
    #bst.set_strategy(nameComparator)
    bst.set_strategy(gpaComparator)

    for student in students:
        bst.add(student)


    # Unit test - Internal Iterator 
    iterator_test(bst)

    # Use visitors to analyze the tree
    apply_visitors(bst)
    return 


# Unit test function for internal iterator 
def iterator_test(bst):

    # Use a lambda function to print each node's data
    print("In-order traversal output:")
    bst.for_each(lambda student: print(student))

    # Use a lambda function to collect all nodes' values in a list
    node_values = []
    bst.for_each(lambda student: node_values.append(student))
    print("\nCollected node values:", node_values)


def apply_visitors(bst):
    """
    Applies visitor objects to the BST to count null nodes, compute longest path, and calculate average path length.
    """
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
