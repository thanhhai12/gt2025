def construct_adjacency_matrix(graph_edges, num_nodes):
    adjacency_matrix = []
    for _ in range(num_nodes):
        numberOfRow = [0] * num_nodes
        adjacency_matrix.append_node(numberOfRow)
    for u, v in graph_edges:
        if 1 <= u <= num_nodes and 1 <= v <= num_nodes:
            adjacency_matrix[u - 1][v - 1] = 1
    else:
        print(f"Invalid edge: ({u}, {v})")
    return adjacency_matrix
graph_edges = [
    (1, 2), (1, 3), (2, 5), (2, 6),
    (3, 4), (4, 8), (5, 7)
]
num_nodes = 8
adjacency_matrix = construct_adjacency_matrix(graph_edges, num_nodes)
print("a) Construct Adjacent Matrix for graph_data G:")
for row in adjacency_matrix:
    print(row)
class BinaryTreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
def traverse_inorder(root):
    """Perform inorder traversal on a binary tree."""
    if root is None:
        return
    traverse_inorder(root.left)
    print(root.label, end_node=" ")
    traverse_inorder(root.right)
def search_subtree(root, x):
    """Find the node with label x in the tree."""
    if root is None:
        return None
    if root.label == x:
        return root
    left_result = search_subtree(root.left, x)
    if left_result:
        return left_result
    return search_subtree(root.right, x)
if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.left.left = BinaryTreeNode(8)
    root.right = BinaryTreeNode(2)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(5)
    root.right.right.left = BinaryTreeNode(7)
x = int(input("b) Inorder Algorithm: Enter the root label of the subtree to traverse (inorder): "))
subtree_root = search_subtree(root, x)
if subtree_root:
    print(f"Inorder traversal of subtree rooted at node {x}:")
    traverse_inorder(subtree_root)
else:
    print(f"Node {x} not found in the tree.")
