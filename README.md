# CS635_project (Advanced Object Oriented Programming: Fall 2024) 
  -  Group Member: Kenichi Sakamoto, Hyunhee Kwak, Dan Houston 

## Assignment1: Trie Tree Implementation 
  -  Language: C++
  -  files: Trie.h, Trie.cpp, main.cpp
  -  To compile: make
  -  Remove executable file: make clean

## Assignment2: BST With Multiple Design Patterns
  -  Language: Python 
  -  Applied Design Patterns
     -  Internal Iterator 
     -  Strategy 
     -  Null Object
     -  Visitor
  -  Project Structure
      ```
      project/
      ├── binary_search_tree.py  # Defines the BinarySearchTree class with internal iterator and strategy pattern
      ├── main.py                # Entry point for using the Binary Search Tree and applying visitors
      ├── null_node_counter.py   # Visitor class to count NullNodes in the BST
      ├── path_metrics_visitor.py # Visitor class to calculate longest and average path length in the BST
      ├── student_data.py        # Defines the Student class and Comparator for sorting strategies
      ├── tree_nodes.py          # Defines TreeNode, NullNode, and TreeNodeInterface for Null Object pattern
      ```
