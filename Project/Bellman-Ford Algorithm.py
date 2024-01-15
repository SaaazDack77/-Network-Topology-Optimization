import numpy as np
import networkx as nx

def read_input_file(file_path):
    # Read the input file and parse the matrices
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    # Separate matrices based on an empty row
    adjacency_str, bandwidth_str, delay_str, reliability_str = '\n'.join(lines).split('\n\n')

    # Parse matrices
    adjacency_matrix = np.array([list(map(int, row.split(':'))) for row in adjacency_str.strip().split('\n')])
    bandwidth_matrix = np.array([list(map(int, row.split(':'))) for row in bandwidth_str.strip().split('\n')])
    delay_matrix = np.array([list(map(int, row.split(':'))) for row in delay_str.strip().split('\n')])
    reliability_matrix = np.array([list(map(float, row.split(':'))) for row in reliability_str.strip().split('\n')])

    return adjacency_matrix, bandwidth_matrix, delay_matrix, reliability_matrix

def bellman_ford_algorithm(graph, source, destination):

    path = nx.bellman_ford_path(graph, source, destination)
    
    # Calculate the distance separately
    distance = nx.bellman_ford_path_length(graph, source, destination)
    return distance, path

def constraints_check(path, bandwidth_matrix, delay_matrix, reliability_matrix):
    if not path:
        return False, False, False  # No path found

    path_edges = list(zip(path[:-1], path[1:]))  # Extract edges from the path

    # Extract bandwidth and reliability values for the edges in the path
    bandwidth_values = [bandwidth_matrix[u][v] for u, v in path_edges]
    reliability_values = [reliability_matrix[u][v] for u, v in path_edges]

    min_bandwidth = np.min(bandwidth_values)
    total_delay = np.sum(delay_matrix[np.array(path)])
    min_reliability = np.min(reliability_values)

    bandwidth_constraint = min_bandwidth >= 5
    delay_constraint = total_delay < 40
    reliability_constraint = min_reliability > 0.70

    return bandwidth_constraint, delay_constraint, reliability_constraint

def create_graph(adjacency_matrix):
    G = nx.DiGraph()
    num_nodes = len(adjacency_matrix)
    G.add_nodes_from(range(num_nodes))
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adjacency_matrix[i][j])  # Adjust weight as needed
    
    return G

def Solution(file_path, source, destination, bandwidth_requirement):
    # Read input file
    adjacency_matrix, bandwidth_matrix, delay_matrix, reliability_matrix = read_input_file(file_path)

    # Create a directed graph using NetworkX
    G = create_graph(adjacency_matrix)

    # Find the shortest path using Bellman-Ford algorithm
    distance, path = bellman_ford_algorithm(G, source, destination)
    
    # Checking constraints for the obtained path
    bandwidth_constraint, delay_constraint, reliability_constraint = constraints_check(
        path, bandwidth_matrix, delay_matrix, reliability_matrix
    )

    if not (bandwidth_constraint and delay_constraint and reliability_constraint):
        print("Path doesn't satisfy constraints:")
        if not bandwidth_constraint:
            print("- Bandwidth constraint not met")
        if not delay_constraint:
            print("- Delay constraint not met")
        if not reliability_constraint:
            print("- Reliability constraint not met")
        return "Path doesn't satisfy constraints."

    print("It works")  # This line indicates everything is fine if reached

    return path  # Return only the path without the distance

# Example usage:
file_path = 'Project/text.txt'
source_node = 20
destination_node = 21
bandwidth_req = 5

result = Solution(file_path, source_node, destination_node, bandwidth_req)
print(result)