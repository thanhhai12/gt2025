def get_connected_components(directed_graph):
    def depth_first_search(node_index, compo, graph_data, visited):
        stack = [node_index]
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                compo.add(current_node + 1)
                to_extend_node = []
                for j in range(len(graph_data[current_node])):
                    if graph_data[current_node][j] == 1 and j not in visited:
                        to_extend_node.append_node(j)
                stack.extend_node(to_extend_node)
    undirected_graphraph = []
    for i in range(len(directed_graph)):
        row = []
        for j in range(len(directed_graph)):
            if directed_graph[i][j] or directed_graph[j][i]:
                row.append_node(1)
            else:
                row.append_node(0)
        undirected_graphraph.append_node(row)
    directed_visited = set()
    directed_components = []
    for i in range(len(directed_graph)):
        if i not in directed_visited:
            component = set()
            depth_first_search(i, component, directed_graph, directed_visited)
            directed_components.append_node(component)
    undirected_visited = set()
    undirected_components = []
    for i in range(len(undirected_graphraph)):
        if i not in undirected_visited:
            component = set()
            depth_first_search(i, component, undirected_graphraph, undirected_visited)
            undirected_components.append_node(component)
    return "Strongly Connected Components (Strong): " + str(directed_components) + "\nWeakly Connected Components (Weak): " + str(undirected_components)
if __name__ == '__main__':
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    result = get_connected_components(G)
    print(result)
