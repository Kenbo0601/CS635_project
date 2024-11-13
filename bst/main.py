from student import Student
from comparator import ComparatorStrategy, ByNameComparator, ByRedIdComparator, ByRoundedGPAComparator
from binary_search_tree import BinarySearchTree
from tree_visitors import VisitorInterface, NullNodeCounter, PathMetricsVisitor

def main():
    """
    Main function to test the Binary Search Tree (BST) with various ordering strategies
    and apply visitor patterns. This demonstrates the Strategy pattern (sorting) and 
    Visitor pattern (analyzing tree properties).
    """
    # List of sample students to be inserted into the Binary Search Tree
    students = [
        Student("John", "Doe", 101, 3.5),
        Student("Jane", "Smith", 102, 3.7),
        Student("Alice", "Johnson", 103, 2.8)
    ]

    # Define multiple comparator strategies to be tested
    strategies = {
        "RedId": ByRedIdComparator(),     # Order by red ID
        "Name": ByNameComparator(),       # Order by last and first name
        "GPA": ByRoundedGPAComparator()   # Order by rounded GPA value
    }

    # Loop over each strategy, create a BST ordered by that strategy, and apply visitors
    for strategy_name, strategy in strategies.items():
        print(f"\n\n--- Testing Order by {strategy_name} Strategy ---")
        
        # Create and populate the BST with the current strategy
        bst = create_and_populate_tree(students, strategy)
        
        # Test the internal iterator (in-order traversal) for correctness
        iterator_test(bst)
        
        # Apply visitor patterns to analyze tree structure
        apply_visitors(bst)


def create_and_populate_tree(students, strategy: ComparatorStrategy):
    """
    Creates a Binary Search Tree, applies a given comparison strategy, and inserts student nodes.
    
    Args:
        students (list): List of Student objects to insert into the BST.
        strategy (ComparatorStrategy): The strategy used to order the students in the BST.
    
    Returns:
        BinarySearchTree: A populated BST with the specified ordering strategy.
    """
    bst = BinarySearchTree()
    bst.set_strategy(strategy)  # Set the comparison strategy for ordering nodes
    for student in students:
        bst.insert(student)  # Insert each student according to the strategy
    return bst  # Return the populated BST


def iterator_test(bst):
    """
    Tests the internal iterator of the Binary Search Tree by performing an in-order traversal.
    The function demonstrates that each node is processed in order.
    
    Args:
        bst (BinarySearchTree): The binary search tree to test.
    """
    print("\n### Iterator Test ###")
    print("---------------------")

    # Print each node's data using in-order traversal
    print("In-order traversal output:")
    bst.for_each(lambda student: print(student))  # Lambda function to print each student's data

    # Collect all nodes' values in a list to verify traversal order and store the result
    node_values = []
    bst.for_each(lambda student: node_values.append(student))  # Lambda function to collect node values
    print("\nCollected node values:", node_values)  # Display collected values for verification


def apply_visitors(bst):
    """
    Applies visitor objects to the BST to analyze structural properties such as 
    the number of null nodes and path metrics. Demonstrates the use of the Visitor pattern.
    
    Args:
        bst (BinarySearchTree): The binary search tree to which visitors are applied.
    """
    print("\n### Visitor Test ###")
    print("--------------------")

    # NullNodeCounter visitor to count the number of null (empty) nodes in the tree
    null_node_counter = NullNodeCounter()
    bst.accept(null_node_counter)  # Pass the visitor to the BST to perform counting
    print("\nNumber of null nodes:", null_node_counter.get_null_count())  # Display the null node count

    # PathMetricsVisitor to calculate and display path metrics (longest and average path lengths)
    path_metrics_visitor = PathMetricsVisitor()
    bst.accept(path_metrics_visitor)  # Pass the visitor to compute path metrics
    print("Longest path length:", path_metrics_visitor.get_longest_path())  # Longest path in the tree
    print("Average path length:", path_metrics_visitor.get_average_path_length())  # Average path length


if __name__ == '__main__':
    main()
