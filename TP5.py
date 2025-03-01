import numpy as np
import heapq
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
num_nodes = len(nodes)
node_to_index = {node: index for index, node in enumerate(nodes)}
adjacency_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
graph_edges = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]
for edge in graph_edges:
    x, y, weight = edge
    i, j = node_to_index[x], node_to_index[y]
    adjacency_matrix[i][j] = weight
    adjacency_matrix[j][i] = weight
adjacency_matrix_np = np.array(adjacency_matrix)
def format_value(x):
    if x == float('inf'):
        return ' inf'
    return f'{int(x):4d}'
formatted_matrix = np.array2string(
    adjacency_matrix_np,
    formatter={'all': format_value},
    separator=' ',
    max_line_width=120
)
print("Adjacency Matrix for Undirected and Weighted graph_data:")
print(formatted_matrix)
index_to_node = {index: node for index, node in enumerate(nodes)}
def dijkstra_shortest_path(adjacency_matrix, source_node, target_node):
    source_node_idx = node_to_index[source_node]
    target_node_idx = node_to_index[target_node]
    distances = [float('inf')] * num_nodes
    distances[source_node_idx] = 0
    prev = [None] * num_nodes
    pq = [(0, source_node_idx)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor in range(num_nodes):
            weight = adjacency_matrix[current_node][neighbor]
            if weight != float('inf'):
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
    path = []
    current = target_node_idx
    while current is not None:
        path.append_node(index_to_node[current])
        current = prev[current]
    path.reverse()
    return path, distances[target_node_idx]
source_node = input("Enter the source_node node (A-M): ").strip().upper()
target_node = input("Enter the target_node node (A-M): ").strip().upper()
if source_node in node_to_index and target_node in node_to_index:
    shortest_path, total_weight = dijkstra_shortest_path(adjacency_matrix, source_node, target_node)
    print(f"Shortest path from {source_node} to {target_node}: {' -> '.join(shortest_path)}")
    print(f"Weighted sum of the shortest path: {total_weight}")
else:
    print("Invalid nodes. Please enter valid node labels (A-M).")
