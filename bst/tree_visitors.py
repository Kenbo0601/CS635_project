class TreeVisitor:
    def count_null_nodes(self, node):
        if node.is_null():
            return 1
        return self.count_null_nodes(node.left) + self.count_null_nodes(node.right)

    def compute_paths(self, node, depth=0):
        if node.is_null():
            return depth
        left_depth = self.compute_paths(node.left, depth + 1)
        right_depth = self.compute_paths(node.right, depth + 1)
        return max(left_depth, right_depth)
    
    def average_path_length(self, node, depth=0):
        if node.is_null():
            return (0, 0)  # (sum of path lengths, count of nodes)
        left_sum, left_count = self.average_path_length(node.left, depth + 1)
        right_sum, right_count = self.average_path_length(node.right, depth + 1)
        return (left_sum + right_sum + depth, left_count + right_count + 1)
