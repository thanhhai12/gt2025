def is_path_available(graph_data, start_node, end_node):
    visited = set()
    def depth_first_search(node):
        if node == end_node:
            return True
        visited.add(node)
        for neighbor in graph_data.get(node, []):
            if neighbor not in visited:
                if depth_first_search(neighbor):
                    return True
        return False
    return depth_first_search(start_node)
def main():
    graph_data = {
        '1': ['2'],
        '2': ['1', '5'],
        '3': ['6'],
        '4': ['6', '7'],
        '5': ['2'],
        '6': ['3', '4', '7'],
        '7': ['4', '6']
    }
    print("Enter the start_node and end_node nodes:")
    start_node = input("Start node: ").strip()
    end_node = input("End node: ").strip()
    if is_path_available(graph_data, start_node, end_node):
        print(f"=> Path exists between {start_node} and {end_node}.")
    else:
        print(f"=> No path exists between {start_node} and {end_node}.")
if __name__ == "__main__":
    main()
