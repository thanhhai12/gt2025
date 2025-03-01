import numpy as np
import heapq
num_nodes = 9
adjacency_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
graph_edges = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8),
    (8, 9, 1),
    (9, 8, 7)
]
for u, v, w in graph_edges:
    adjacency_matrix[u - 1][v - 1] = w
    adjacency_matrix[v - 1][u - 1] = w
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
def prim_mst(adjacency_matrix, root):
    n = len(adjacency_matrix)
    visited = [False] * n
    min_heap = [(0, root, -1)]
    mst_graph_edges = []
    total_weight = 0
    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight
        if parent != -1:
            mst_graph_edges.append_node((parent + 1, node + 1, weight))
        for neighbor in range(n):
            if not visited[neighbor] and adjacency_matrix[node][neighbor] > 0:
                heapq.heappush(min_heap, (adjacency_matrix[node][neighbor], neighbor, node))
    return mst_graph_edges, total_weight
def kruskal_mst(adjacency_matrix):
    n = len(adjacency_matrix)
    graph_edges = [
        (adjacency_matrix[i][j], i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if adjacency_matrix[i][j] > 0
    ]
    graph_edges.sort()
    parent = list(range(n))
    rank = [0] * n
    mst_graph_edges = []
    total_weight = 0
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    for weight, u, v in graph_edges:
        if find(u) != find(v):
            union(u, v)
            mst_graph_edges.append_node((u + 1, v + 1, weight))
            total_weight += weight
    return mst_graph_edges, total_weight
root_node = int(input("\nEnter the root node for Prim's algorithm: ")) - 1
prim_graph_edges, prim_weight = prim_mst(adjacency_matrix, root_node)
kruskal_graph_edges, kruskal_weight = kruskal_mst(adjacency_matrix)
print("\nPrim's Algorithm MST:")
for edge in prim_graph_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {prim_weight}")
print("\nKruskal's Algorithm MST:")
for edge in kruskal_graph_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {kruskal_weight}")
